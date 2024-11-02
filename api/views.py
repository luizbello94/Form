from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import send_message,responder_consulta
import logging


logger = logging.getLogger(__name__)

@api_view(['GET'])
def get_api(request):
    return Response({"System":"online"})


@api_view(['POST'])
def post_message(request):
    from_data = request.data
    from_number = from_data.get('From','')
    if "whatsapp:" in from_number:
        whats_app_number = from_number.split("whatsapp:")[-1]
    else:
        logger.error(f'Invalid whatsapp number')
        return Response({"Error":"Invalid whatsapp number"},status=400)
    logger.info(f"Message of {whats_app_number} was received")
    body = from_data.get('Body','').strip()
    if not body:
        logger.info(f'Empty message from number {whats_app_number}')
        send_message(whats_app_number,"Please send more details so I can assist you.")
        return Response({"status":"success", "message": "Prompted user for more details"})
    else:
        respuesta_mensaje = responder_consulta(body)
        send_message(whats_app_number,respuesta_mensaje)
    return Response({"System":"Send message","message": "Message sent to WhatsApp number"})