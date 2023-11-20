# Reto-IA-Avanzada-2

## Objetivo

Nuestro objetivo principal es generar una solución completa utilizando ciencia de datos e inteligencia artificial, siguiendo la metodología CRISP-DM (Cross Industry Standard Process for Data Mining). Durante 11 semanas, nos sumergiremos en etapas clave para abordar un desafío propuesto por nuestro socio formador, Arca Continental, líder en la industria de bebidas.

Arca Continental busca una solución de inteligencia artificial que genere contenido textual y visual para utilizar en campañas publicitarias de sus productos. La idea es que esta IA sea capaz de crear descripciones atractivas y creativas, así como diseñar imágenes relacionadas con las bebidas que ofrecen.

- **Comprensión del Negocio:** Estableceremos expectativas y criterios de aceptación, planificaremos recursos y evaluaremos posibles riesgos, centrándonos en la industria de bebidas y la publicidad.

- **Preparación de Datos:** Obtendremos, exploraremos y prepararemos los datos relacionados con el mercado de bebidas y campañas publicitarias, aplicando transformaciones y procesos esenciales para análisis posteriores.

- **Modelado y MVP:** Utilizaremos los datos para generar un modelo inicial que permita la creación automática de descripciones y diseños de imágenes atractivos para publicidad.

- **Mejora Continua y MBI's:** Iteraremos para mejorar el modelo y ajustaremos la plataforma según las necesidades específicas de Arca Continental, optimizando la generación de contenido y la creatividad en las imágenes.

- **Despliegue:** Planificaremos y ejecutaremos el despliegue de la plataforma en un ambiente de pre-producción, utilizando arquitectura en la nube y garantizando que esté accesible para el equipo de Arca Continental.


## Contenido dentro del repositorio
**1. Propuesta inicial**
Nuestra propuesta se basa en la creación de un Chatbot donde se pueda introducir información relevante de acuerdo al artículo promocional (precio, descuento, nombre del artículo, imagen del artículo o artículos) como input, y el póster promocional relativo al artículo como output. 

**2. Protipo Llama2**
Llama 2 es altamente adaptable y versátil, especializándose en la generación de texto para una amplia gama de aplicaciones. Elección ideal tanto para investigadores como para empresas que buscan generar contenido escrito de manera efectiva y personalizable.

**3. Codigo Generativo**
Luna Diffusion 2.5 se destaca por su capacidad para convertir descripciones textuales en arte y representaciones visuales, atrayendo a la comunidad artística y comercial. Es una herramienta innovadora que genera imágenes a partir de texto, siendo un avance significativo en esta tecnología.

**4. Aplicación**
Se utilizo Streamlit para crear una interfaz donde los usuarios pueden ingresar detalles de un producto promocional. Utiliza un modelo de inteligencia artificial llamado "StableDiffusionPipeline" para generar imágenes promocionales basadas en la entrada del usuario. Una vez que se ingresan los detalles, el código utiliza el modelo para crear y mostrar las imágenes en la interfaz de usuario.
