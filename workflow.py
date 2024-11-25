from patient import create_patient_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir
from base import get_resource_by_document_number  # Asegúrate de importar la nueva función
from condition import create_condition_resource

if __name__ == "__main__":
    # Parámetros del paciente
    document_number = "43874953"  # Ejemplo de número de documento
    family_name = "Alvarez"
    given_name = "Victoria"
    birth_date = "2002-03-06"
    gender = "female"
    phone = "1160329204"

    # Crear y enviar el recurso de paciente
    patient = create_patient_resource(document_number, family_name, given_name, birth_date, gender, phone)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')

    # Ver el recurso de paciente creado
    if patient_id:
        print(f"Recurso creado con ID: {patient_id}")
        get_resource_from_hapi_fhir(patient_id, 'Patient')

    # Buscar el paciente por documento
    print(f"Buscando paciente con documento {document_number}...")
    get_resource_by_document_number(document_number, 'Patient')
    
    # Crear el recurso Condition con los parámetros dados
    condition_resource = create_condition_resource(
        condition_code="Diabetes tipo 2",
        patient_id="12345",
        condition_status="active",
        onset_date="2020-01-01",  # Usar formato string adecuado
        end_date="2025-01-01",    # Usar formato string adecuado
        condition_id="condition123"
    )
    # Enviar el recurso de dispositivo
    condition__id = send_resource_to_hapi_fhir(condition_resource, 'Condition')
    # Imprimir el recurso creado
    print(condition_resource)

    # Ver el recurso de dispositivo creado
    if condition__id:
        get_resource_from_hapi_fhir(condition_resource, 'Condition')

    print("\n")
