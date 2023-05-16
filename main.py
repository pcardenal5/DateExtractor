### Import necessary libraries ###
from transformers import AutoTokenizer, MarianMTModel, RobertaForQuestionAnswering
import torch
from ExtractDateService import *

### Functions ###
def extract_date(text):
    DateExtract=ExtractDate(text=text)
    print(DateExtract.StartExtraction(), '\n')


### Main ###
if '__main__' == __name__:

    short_texts = ['Nos vemos el próximo martes, 21/05/23, para discutir los detalles del proyecto.',
                   'El concierto de tu banda favorita será el 10 de junio de este año. ¡No te lo puedes perder!',
                   'El plazo de entrega de la tarea es el 1 de julio. Recuerda enviarla a tiempo.',
                   '¡Feliz aniversario! Hoy celebramos 15 años juntos, desde el 12-05-2008.',
                   'La conferencia internacional se llevará a cabo del 5 al 7 de agosto. ¡Prepárate para aprender mucho!']
    
    mid_texts = ['¡Estoy emocionado! El próximo viernes, 28 de septiembre de 2023, se llevará a cabo el festival de música más grande de la ciudad. Habrá bandas en vivo, food trucks y actividades para toda la familia. No puedo esperar para disfrutar de una noche llena de diversión y buena música.',
                 '¡Atención, amantes del fútbol! Marquen en sus calendarios el 5 de mayo de 2023, porque ese día se disputará la final de la Copa Libertadores. Los equipos más destacados de América se enfrentarán en un duelo épico por el título. Será un evento deportivo que no querrán perderse.',
                 'Querida abuela, este año celebraremos tu cumpleaños número 80 el 10 de noviembre. Te estamos organizando una fiesta sorpresa en el jardín de casa, con la presencia de familiares y amigos cercanos. Será un día lleno de alegría, recuerdos y amor. Esperamos verte allí para compartir este momento especial contigo.',
                 'Queridos padres de familia, les informamos que la reunión de padres y maestros para el segundo trimestre se llevará a cabo el miércoles 26 de noviembre a las 18:00 horas. En esta reunión, tendrán la oportunidad de conversar con los profesores y recibir información importante sobre el progreso académico de sus hijos. Por favor, asegúrense de asistir.',
                 '¡Atención estudiantes! El plazo para la entrega de los proyectos finales se ha extendido hasta el viernes 5 de diciembre. Aprovechen este tiempo adicional para completar y perfeccionar sus proyectos. Recuerden que la calidad y originalidad serán tenidas en cuenta en la evaluación. ¡Mucho éxito!']
    
    long_texts = ['Descubrimiento de América es la denominación que recibe el acontecimiento histórico acaecido el 12 de octubre de 1492, consistente en la llegada a América de una expedición proveniente de Castilla, en la península ibérica, dirigida por Cristóbal Colón por mandato de los Reyes Católicos, Isabel de Castilla y Fernando de Aragón. Colón había partido del Puerto de Palos dos meses y nueve días antes y, tras cruzar el océano Atlántico, llegó a una isla del continente americano, Guanahani, creyendo que había llegado a la India. Este hecho es uno de los momentos fundamentales de la historia universal y representa un «descubrimiento» para las personas que vivían en Afroeurasia de culturas, civilizaciones, escrituras, idiomas, tecnologías, productos, cultivos, ganados, ciudades, riquezas, fauna y flora, buena tierra, condiciones climáticas favorables al europeo y no europeo, y de una población con una cosmología de relaciones de poder muy distintas; así como el llamado «encuentro de dos mundos» que habían evolucionado independientemente desde el poblamiento de América.',
                  'El 20 de julio de 1969 quedará grabado en la memoria colectiva como el día en que la humanidad alcanzó la Luna por primera vez. Fue en esta fecha que la misión Apolo 11, conformada por los astronautas Neil Armstrong, Buzz Aldrin y Michael Collins, logró aterrizar en la superficie lunar. El mundo entero siguió con atención cada paso de aquel histórico alunizaje, y millones de personas se congregaron frente a sus televisores para presenciar el momento en que Armstrong dio el famoso paso y pronunció las icónicas palabras: "Es un pequeño paso para el hombre, pero un gran salto para la humanidad". Este logro científico y tecnológico sin precedentes marcó un hito en la exploración espacial y dejó una huella imborrable en la historia de la humanidad.',
                  'El 9 de noviembre de 1989 es una fecha que se encuentra grabada en la historia como el día en que cayó el Muro de Berlín. Después de casi tres décadas de dividir a la ciudad de Berlín y a Alemania en dos, esta fecha marcó un momento de unificación y esperanza. Miles de personas se congregaron frente al muro y, con martillos y picos en mano, comenzaron a derribarlo, símbolo tangible de la Guerra Fría. El derribo del muro no solo permitió la reunificación de Alemania, sino que también simbolizó el fin de una era de divisiones y el inicio de un nuevo capítulo en la historia europea.',
                  'El 4 de julio de 1776 es una fecha trascendental en la historia de los Estados Unidos. Fue en ese día que se firmó la Declaración de Independencia, en la cual las Trece Colonias proclamaron su separación formal del dominio británico. Esta fecha marca el nacimiento de una nación independiente y el comienzo de una lucha por los ideales de libertad y autogobierno. Cada año, el 4 de julio se celebra como el Día de la Independencia en Estados Unidos, con desfiles, fuegos artificiales y eventos conmemorativos en todo el país. Esta fecha representa un recordatorio del valor de la independencia y la lucha por los derechos y la libertad.',
                  'El 12 de octubre de 1492 es una fecha histórica que marcó el inicio de un nuevo capítulo en la historia mundial. Fue en ese día que Cristóbal Colón y su tripulación llegaron a América, creyendo haber alcanzado las Indias. Este encuentro fortuito entre Europa y el continente americano abrió las puertas a la exploración, el intercambio cultural y la colonización que transformarían el curso de la historia. El 12 de octubre se celebra en muchos países de América Latina como el Día de la Hispanidad, el Día de la Raza o el Día de la Resistencia Indígena, con el objetivo de reflexionar sobre los diferentes aspectos de este encuentro y su impacto en las sociedades actuales.']
    
    texts = {'SHORT': short_texts, 'MID': mid_texts, 'LONG': long_texts}

    for key, value in texts.items():
        print(f'### {key} TEXTS ###', '\n')
        for text in value:
            extract_date(text)