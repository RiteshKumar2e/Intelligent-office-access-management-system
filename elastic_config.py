from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")  # Assuming locally running

# Sample function to sync MongoDB employee to Elastic
def index_employee(employee_data):
    es.index(index="employees", id=employee_data['emp_id'], body={
        "name": employee_data['name'],
        "face_encoding": employee_data['face_encoding'],
        "emp_id": employee_data['emp_id']
    })
