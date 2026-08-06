import os
import xml.etree.ElementTree as ET
import pandas as pd
import requests

# ID del BioProject Ganador (Metástasis de Cáncer de Mama scRNA-seq)
BIOPROJECT_ID = "PRJEB108071"


def get_sra_metadata(bioproject_id):
    print(
        f"🔍 Extrayendo metadatos vírgenes del estudio de metástasis: {bioproject_id}..."
    )

    # Consulta a la API de NCBI/ENA
    esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term={bioproject_id}&retmode=json"
    res = requests.get(esearch_url).json()

    id_list = res.get("esearchresult", {}).get("idlist", [])
    print(
        f"✅ ¡Conexión exitosa! Se encontraron {len(id_list)} muestras/experimentos moleculares en el proyecto."
    )

    if not id_list:
        print("❌ No se encontraron registros para este ID.")
        return

    # Traer detalles de metadatos XML
    efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=sra&id={','.join(id_list)}&retmode=xml"
    xml_data = requests.get(efetch_url).content

    root = ET.fromstring(xml_data)
    samples_summary = []

    for item in root.findall(".//EXPERIMENT_PACKAGE"):
        run_acc = item.find(".//RUN").attrib.get("accession", "N/A")
        biosample = item.find(".//SAMPLE").attrib.get("accession", "N/A")

        # Título y descripción del órgano objetivo (Cerebro, Hígado, Pulmón, Hueso)
        title_node = item.find(".//SAMPLE/TITLE")
        sample_title = title_node.text if title_node is not None else "N/A"

        attributes = {}
        for attr in item.findall(".//SAMPLE_ATTRIBUTE"):
            tag = attr.find("TAG")
            val = attr.find("VALUE")
            if tag is not None and val is not None:
                attributes[tag.text.strip().lower()] = val.text.strip()

        samples_summary.append(
            {
                "Run_Accession": run_acc,
                "BioSample": biosample,
                "Sample_Title": sample_title,
                "Organ_Target": attributes.get(
                    "tissue", attributes.get("organism_part", "N/A")
                ),
                "Attributes": str(attributes),
            }
        )

    df = pd.DataFrame(samples_summary)

    os.makedirs("data", exist_ok=True)
    output_path = "data/metastasis_metadata.csv"
    df.to_csv(output_path, index=False)

    print(f"💾 Metadatos guardados correctamente en '{output_path}'")
    print("\n📋 Primeras 5 muestras del atlas de metástasis:")
    print(df[["Run_Accession", "Sample_Title", "Organ_Target"]].head())


if __name__ == "__main__":
    get_sra_metadata(BIOPROJECT_ID)