from django.core import mail
from celery import shared_task



@shared_task
def preparate_and_send_email(prep):
       
    with mail.get_connection() as connection:
        mail.EmailMessage(
            f"Письмо от {prep['name']} email {prep['email']}",
            f'Тип работ: {prep["work_type"]}\n Материал стен: {prep["material_type"]}\n Вопрос:\n {prep["question"]}',
            'gas53@internet.ru',
            ['gas53@bk.ru'],
            connection=connection,
            ).send()