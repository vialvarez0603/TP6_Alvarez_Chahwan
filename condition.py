from fhir.resources.condition import Condition
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.identifier import Identifier
from fhir.resources.reference import Reference

# Crear el recurso FHIR de condición con parámetros opcionales
def create_condition_resource(condition_code=None, patient_id=None, condition_status=None, onset_date=None, end_date=None, id=None):
    # Crear una instancia del recurso Condition
    condition = Condition()

    # Asignar un identificador único para la condición
    if id:
        identifier = Identifier()
        identifier.system = "http://example.org/fhir/condition/id"
        identifier.value = id
        condition.identifier = [identifier]

    # Agregar el código de la condición si está disponible
    if condition_code:
        code = CodeableConcept()
        code.text = condition_code
        condition.code = code

    # Asignar el estado de la condición (por ejemplo, 'active', 'resolved')
    if condition_status:
        condition.clinicalStatus = CodeableConcept(text=condition_status)

    # Asignar las fechas de inicio y fin de la condición, si están disponibles
    if onset_date:
        condition.onsetDateTime = onset_date  # Utilizando formato string "YYYY-MM-DD"
    if end_date:
        condition.abatementDateTime = end_date

    # Agregar la referencia al paciente
    if patient_id:
        patient_ref = Reference()
        patient_ref.reference = f"Patient/{patient_id}"
        condition.subject = patient_ref

    return condition
