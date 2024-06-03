from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter


trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
tracer = trace.get_tracer(__name__)


# create an instance of the API class
configuration = swagger_client.Configuration()
configuration.host = 'http://192.168.20.217:8080/api/v1'
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

try:
    with tracer.start_as_current_span("E-catalog-category"):
        # Получить список всех категорий
        api_response = api_instance.category_get()
        pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->category_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.Category() # Category |

try:
    with tracer.start_as_current_span("E-catalog-newItemAdd"):
        # Добавить новую категорию
        api_instance.category_post(body)

except ApiException as e:
    print("Exception when calling CategoriesApi->category_post: %s\n" % e)