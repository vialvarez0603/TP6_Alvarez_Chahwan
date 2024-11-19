import requests
from patient import create_patient_resource


# Enviar el recurso FHIR al servidor HAPI FHIR
def send_resource_to_hapi_fhir(resource,resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}"
    headers = {"Content-Type": "application/fhir+json"}
    resource_json = resource.json()

    response = requests.post(url, headers=headers, data=resource_json)

    if response.status_code == 201:
        print("Recurso creado exitosamente")
        
        # Devolver el ID del recurso creado
        return response.json()['id']
    else:
        print(f"Error al crear el recurso: {response.status_code}")
        print(response.json())
        return None

# Buscar el recurso por ID 
def get_resource_from_hapi_fhir(resource_id, resource_type):
    url = f"http://hapi.fhir.org/baseR4/{resource_type}/{resource_id}"
    response = requests.get(url, headers={"Accept": "application/fhir+json"})

    if response.status_code == 200:
        resource = response.json()
        print(resource)
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())
def get_resource_by_document_number(document_number, resource_type):
    # Definir la URL de búsqueda utilizando el número de documento
    url = f"https://launch.smarthealthit.org/v/r4/fhir//{resource_type}?identifier={document_number}"
    
    # Realizar la solicitud GET al servidor FHIR con los encabezados apropiados
    response = requests.get(url, headers={"Accept": "application/fhir+json"})
    
    # Verificar la respuesta
    if response.status_code == 200:
        resources = response.json()
        
        # Verificar si se encontró algún recurso
        if 'entry' in resources:
            for entry in resources['entry']:
                print(entry['resource'])  # Imprime el recurso encontrado
        else:
            print("No se encontraron recursos con ese número de documento.")
    else:
        print(f"Error al obtener el recurso: {response.status_code}")
        print(response.json())  # Mostrar detalles del error si lo hay
