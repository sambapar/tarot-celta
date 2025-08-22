# -*- coding: utf-8 -*-
"""
Created on Fri Aug 15 10:43:41 2025

@author: samuel
"""

def tarot_celta(tirada,orient):
    """
    Parameters
    ----------
    tirada : TYPE: array con números enteros que representan las cartas de la tirada en orden.
    orient : TYPE: array con letras que representan si la carta está del derecho (d) o del revés (r).

    Returns: interpretación de la tirada celta.
    -------
    """
    res=""
    for i in range(0,10):
        if i==0:
            res += "PRIMERA CARTA: la situación en el presente.\n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): indica un nuevo comienzo y la energía de espontaneidad que influye ahora. Esta carta sugiere que hay libertad y confianza y que puedes aprovechar recursos internos para avanzar. Impulsa a tomar una actitud activa y creativa, buscando oportunidades y actuando con intención.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): muestra bloqueo o distorsión de un nuevo comienzo; la energía está atenuada o mal dirigida. Puede señalar dudas, imprudencia o decisiones precipitadas que impiden el avance esperado. Es un aviso a la gestión de la impulsividad y la ruptura del equilibrio riesgo-cuidado para lograr reconducir la situación con consciencia y acciones concretas.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): indica voluntad y la capacidad de poner recursos en acción. Sugiere que cuentas con habilidades y herramientas para influir en lo que ocurre alrededor. Invita a la iniciativa, a usar la creatividad y a manifestar intenciones con claridad. Es el momento de concentrarte y dirigir tu energía hacia objetivos concretos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): muestra bloqueo o manipulación de la voluntad; los recursos no se están empleando con eficacia. Puede indicar inseguridad, falta de enfoque o intentos de controlar situaciones desde la astucia y el beneficio personal en lugar de la honestidad. Es necesario revisar estrategias y restablecer la ointegridad en las acciones.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): indica la intuición y atención a lo que no es evidente. Esta carta sugiere que el conocimiento interno y la reflexión son claves para analizar correctamente la situación presente. Invita a escuchar a tus sueños, sensaciones y señales sutiles antes de actuar. La pausa contemplativa prepara decisiones más sabias y alineadas con tu verdad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): muestra bloqueo del acceso a la intuición o una confusión interna, silenciando tu veradero ser. Puede indicar aislamiento emocional, secretos no abordados o negación de señales importantes. Sugiere la necesidad de reconectar con la escucha interna y frenar la impulsividad externa, recuperar la calma y la atención en pos de la claridad.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): indica creatividad y abundancia que nutre el presente. Hay fertilidad de ideas, afecto y cuidado que sostienen el proceso que tienes entre manos. Invita a cultivar lo que crece a tu alrededor con ternura. Pone énfasis en la receptividad para lograr la prosperidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): muestra bloqueos en la creatividad o descuido en el autocuidado, que limitan fuertemente la abundancia. Puede señalar procrastinación, sentimiento de asfixia o falta de atención a las necesidades básicas. Apremia a restablecer límites sanos y nutrirse en la paciencia del proceso para recuperar la capacidad de crear positivamente y de sostener.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): sugiere estructura y autoridad en el momento actual. Esta carta se asocia con el orden, la disciplina y la claridad en la toma de decisiones que sostienen la situación. Invita a asumir responsabilidades sin miedo, a planificar con firmeza y a establecer límites necesarios. La presencia de dirección y organización facilita el avance seguro.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): muestra rigidez mal aplicada o enfocada o un grave bloqueo hacia las figuras de autoridad presentes. El control se vuelve un obstáculo en el desarrollo personal y social. Puede indicar abuso de poder, excesiva intransigencia o falta de un liderazgo efectivo. Apremia a felxibilizar posturas (no necesariamente propias), delegar adecuadamente y revisar el sistema de poder existente para lograr la estabildiad real.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): carta asociada a la tradición y las normas. Indica valores compartidos por un grupo de personas y aprendizaje formal o espiritual. Invita a buscar consejo, a respetar ritos o a integrar enseñanzas con discernimiento. La conexión con una comunidad o mentor puede aportar sentido al momento presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): muestra bloqueo con instituciones, dogmas o resistencia y cuestionamiento de la tradición. Puede señalar una crisis interna referente a las creencias internas, conflicto con las normas establecidas o necesidad de autonomía. Apremia fuertemente a la revisión del sistema moral imperante para hallar un camino personal que conduzca a la liberación.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): decisiones vinculadas al corazón y la armonía en las relaciones. Esta carta sugiere que las elecciones con base en valores personales y conexión afectiva son centrales en tu vida ahora. Invita a alinear la acción con el amor y la autenticidad, priorizando la sinceridad para una mayor coherencia personal.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): grave incapacidad para tomar decisiones afectivas o conflicto entre deseo y saber. Puede señalar indecisión, tentaciones contrapuestas o falta de compromiso claro hacia los demás. Es un aviso para clarificar prioridades y enfrentar ambivalencias internas con honestidad. Tomar responsabilidad emocional mejorará tu situación.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): avance decidido y control de las adversidades. Es una carta ligada a la determinación por lograr objetivos claros y disciplina en el proceso. Invita a canalizar energía y concentración para superar los obstáculos que te separan de tus metas.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): incapacidad de avanzar por falta de dirección o conflictos internos. Puede sugerir pérdida del control, dispersión o choques de intereses que frenan tu desarrollo. Hay que reenfocar los objetivos, alinear intenciones y recuperar disciplina.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): indica coraje sereno y compasión frente a las dificultades que se te presentan. Dominio interno, paciencia y capacidad para afrontar miedos con suavidad. Invita a confiar en las propias capacidades y sobre todo en la fortaleza emocional antes que en la fuerza bruta.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): ausencia de valor interior o relaciones impulsivas que debilitan la estabilidad de tu situación. Puede señalar inseguridad, pérdida de paciencia o abuso de la fuerza física. Hay que trabajar la autocompasión y la regulación emocional para recuperar el norte y la eficacia.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): tiempo de introspección y búsqueda del sentido de tu vida. Carta asociada al retiro voluntario y a la refelxión profunda para encontrar la valentía necesaria. Prioriza la soledad productiva y la sabiduría que emerge del silencio para arrojar luz sobre los siguientes pasos a seguir.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): aislamiento excesivo que impide el crecimiento personal. Puede indicar una soledad dolorosa, desconexión absoluta o resistencia a pedir ayuda. Apremia a balancear retiro con apertura y a compartir experiencias e inquietudes con personas de confianza.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): indica cambios y ciclos que se ponen en marcha ahora. Sugiere que las circunstancias externas de tu vida están modificando el rumbo. Invita a adaptarse, reconocer oportunidades y aprovechar giros favorables. Analiza la naturaleza de los cambios para obtener el máximo beneficio.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): resistencia al cambio o frustración proveniente del sentimiento de un presente monótono y repetitivo. Puede señalar mala racha, falta de adaptación a nuevas condiciones o fatalismo. Necesitas buscar cómo romper patrones y recuperar tu flexibilidad ante los cambios inevitables.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): indica equilibrio y decisiones basadas en la verdad y la responsabilidad. Esta carta sugiere que asuntos legales o éticos y la necesidad de mantenerte imparcial están en juego. Invita a evaluar los hechos con absoluta honestidad y a asumir las consecuencias resultantes.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): momento presente resultante de decisiones parciales, falta de información o injusticias. Puede indicar un carácter sesgado, dilación legal o evasión de responsabilidades. Es necesario recabar pruebas, analizarlas con honestidad, revisar prejuicios y actuar con equidad.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): pausa intencional, invitación a cambiar de perspectiva. Necesitas ver la situación desde otros ángulos para comprenderla en su totalidad. Invita a soltar la urgencia y a aceptar el sacrificio del tiempo de reflexión como vía de crecimiento. Nuevas opciones antes ignoradas fruto de ello.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): resistencia al cambio o bloqueo por estancamiento. Puede indicar sacrificios inútiles, inmovilismo o renuncia a soltar. Tienes que identificar qué se sostiene por costumbre y qué requiere liberación para desbloquear tu presente.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): transformación profunda y cierre de ciclos necesario. Algo está terminando para dejar lugar a lo nuevo, con alto potencial de renovación si la actitud ante ello es adecuada. Invita a aceptar el proceso de duelo y a confiar en la regeneración del cambio, logrando un mayor grado de autenticidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): miedo profundo a dejar ir. Esto da lugar a estancamiento, negación de procesos naturales y un gran apego a lo conocido que generará gran dolor en el futuro. Apremia fuertemente a confrontar la pérdida y soltar lo que ya no sirve para poder desarrollarte adecuadamente.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): equilibrio vital, procesos de sanación en marcha. Carta ligada a la moderación, mezcla de fuerzas opuestas y ajuste gradual hacia la armonía. Sugiere que te enfoques en la paciencia e integres los extremos con prudencia.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): falta de armonía entre las partes de un todo, lo que conduce al fracaso de proyectos. Impaciencia, mezclas poco saludables que generan conflictos desagradables. Hay que readaptar hábitos y buscar ritmos más sostenibles para lograr un mayor grado de seguridad y plenitud.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): ataduras y desencadenantes materiales o emocionales actualmente. Presencia de tentaciones o dependencias que condicionan tu situación. Invita a tomar conciencia de las cadenas autoimpuestas y a trabajar en la liberación para recuperar tu autonomía.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): te encuentras en bloqueo por intensificación de hábitos destructivos o un materialismo feroz. Puede señalar autoengaños, culpabilidad o continuas tentaciones a las que te cuesta negarte. Es el momento de cortar lazos tóxicos y buscar ayuda si es necesario.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): crisis reveladora y súbita. Rupturas que precipitan un cambio radical. Carta fuertemente ligada a las estructuras frágiles, cayendo para exponer verdades incómodas que permitirán una futura reconstrucción. Invita a aceptar la sacudida como una oportunidad de limpieza y renovación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): situación catsatrófica por una conservación brutal de estructuras obsoletas. Puede sugerir negación de la necesidad de cambio, aguante peligroso o búsqueda de conflictos. Incapacidad para cambiarse a uno mismo sin enjerencias externas.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): indica esperanza, inspiración y guía renovadora. La confianza del proceso y la conexión con el sentido elevan la situación presente. Invita a abrirse a la curación, a volver a soñar y a confiar.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): sentimiento de desaliento que te nubla. Puede significar pérdida de fe, idealización de la realidad que resulta dañina o un alto grado de desconexión con la realidad. Carta que a veces puede indicar fenómenos paranormales.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): lo inconsciente, las emociones y las ilusiones tienen un gran papel en tu momento presente. Miedos, sueños y confusiones emergen para ser explorados. Presta atención a tus emociones, señales simbólicas y trata de leer entre líneas.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): puede indicar paranoia, autoengaño o la necesidad de aclarar malentendidos (incluso con uno mismo). La Luna es altamente emocional, luego se recomienda buscar la verdad de forma práctica y recuperar el control de tu mundo interno, comprendiendo la emocionalidad desbordada que te asfixia.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): claridad, éxito y energía positiva que iluminan tu presente. Sugiere optimismo, vitalidad y resultados favorables, fruto del esfuerzo y la coherencia. Invita a celebrar logros, compartir alegría y alimentar tu confianza.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): exceso de orgullo, agotamiento o expectativas no cumplidas. La luz está velada por las dudas o por la dependencia de aprobación externa. Exige reconectar con la autenticidad y ajustar expectativas de forma realista para restablecer el optimismo.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): indica evaluación y una llamada a la toma de consciencia. Es el momento de revisar tu pasado y ejecutar las decisiones que marquen un nuevo comienzo consciente. Invita a asumir responsabilidades y consecuencias de los actos propios y a responder con integridad a las dificultades.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): juicios prematuros o infundados o sentimiento de culpa paralizante. Resistencia a responsabilizarse, overthinkeo de los errores del pasado que te mantienen estancado. Apremia al perdón y la honestidad para permitir el cambio renovador.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): culminación, integración y sensación de realización. Sugiere la completitud de fases, la existencia de una visión global de la situación e invita a disfrutar del logro y a preparase para nuevos ciclos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): sentimiento de final incompleto o frustración por esfuerzos inútiles. Puede indicar que faltan detalles por resolver para cerrar el ciclo. Hay que revisar qué falta para completar la obra y alcanzar la plenitud.\n"
                    continue
        elif i==1:
            res += "SEGUNDA CARTA: el bloqueo. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): la fuerza bloqueadora es la impulsividad o falta de dirección disfrazada de libertad. Ausencia de un plan, generando parálisis práctica.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): la fuerza bloqueadora es el miedo irracional. Urge transformar los temores en curiosidad consciente.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): el obstáculo es la dispersión de los recursos o dificultad para concentrar la voluntad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): el obstáculo es la manipulación, engaño o falta de confianza en las propias capacidades.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): la fuerza bloqueadora es la falta de atención a la voz interior.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): la fuerza bloqueadora es el exceso de secretos no comprendidos (exceso de confianza en la intuición sin pruebas físicas).\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): el obstáculo reside en la falta de cuidado, falta de nutrición de tus proyectos (exceso de frialdad).\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): el obstáculo es el agotamiento (físico, mental o emocional), la sobreprotección o el descuido emocional propio.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): el problema puede ser exceso de rigidez, inflexibilidad, orden demasiado estricto...\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): el problema reside en la desorganización, falta de límites o la acumulación de poder abusiva.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): la fuerza bloqueadora podría ser una moral rígida e inamovible que resulta inservible actualmente o un conformismo exacerbado (falta de innovación).\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): la fuerza bloqueadora es la rebeldía sin propósito, o el afán por la destrucción de estructuras de poder que sí son efectivos y necesarios.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): la barrera es la indecisión, decisiones pendientes o la necesidad de alinear valores.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): la barrera proviene de relaciones desequilibradas, que resultan altamente limitantes y voraces, engaños o falsas elecciones personales que en realidad surgen de la presión externa.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): el obstáculo se encuentra en la falta de coordinación de fuerzas o en ausencia de objetivos claros.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): el obstáculo se encuentra en la pérdida efectiva del control de la situación o la incapacidad de tomar el poder.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): la limitación podría ser la falta de valentía o de confianza, fruto de la necesidad de sentirte seguro.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): la limitación es un exceso de reaccionarismo o de violencia.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): la fuerza bloqueadora se encuentar en la falta de introspección o una actitud exageradamente pasiva.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): la fuerza bloqueadora es la soledad que causa dolor, la incapacidad para integrarse...\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): la barrera puede ser la resistencia a aceptar los giros del destino, por confianza excesiva en la planificación meticulosa.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): la barrera proviene de la mala gestión de las oportunidades por la incapacidad de aprender de ciclos pasados.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): el obstáculo es la ausencia de verdad imperante o la necesidad de asumir responsabilidades aun por enfrentar.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): el obstáculo reside en la parcialidad en las decisiones o la ausencia de una autoridad capaz de decidir de forma justa.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): la limitación reside en la omisión de seguir explorando opciones antes de actuar. Exige pausa y cambio de perspectiva.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): la limutación es la incapacidad de enfocar los sacrificios y esfuerzos de forma correcta.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): la fuerza bloqueadora es el final de una situación aun no identificada, que debe acabar para permitir la renovación y el desarrollo correcto.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): la fuerza bloqueadora es un apego excesivo a lo conocido. Negación prolongada de procesos necesarios o miedo a la pérdida.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): la barrera resulta de la ausencia de equilibrio entre las partes de un todo o de procesos de sanación inconclusos.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): la barrera es el histrionismo que surge ante los problemas, la impaciencia o una actitud demasiado combativa.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): el obstáculo está en la dependencia exagerada del mundo material, que encadena la voluntad (recaídas, desilusiones...).\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): el obstáculo surge de la negación de los aspectos sombríos de las personalidades.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): la limitación consiste en una acumulación de tensión por incapacidad de cambio que se acumula hasta provocar un efecto rebote destructivo que obliga a la transformación súbita.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): la limitación reside en la actitud laxa ante las crisis, la procrastinación o la negación de la necesidad de cambio.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): la fuerza bloqueadora es la falta de confianza o de esperanza o un pesimismo demasiado prolongado.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): la fuerza bloqueadora es el cinismo o el agotamiento espiritual resultante de una cadena de desilusiones.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): la barrera parte del inconsciente, que genera dudas y miedos irracionales.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): la barrera está en una emocionalidad desbordante, que impide el funcionamiento racional de las personas.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): el obstáculo es el exceso de optimismo o la dependencia de la validación externa.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): el obstáculo es el exceso de pesimismo, falta de claridad o sensación constante de fracaso.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): la limitación está en evitar la reflexión o en posponer decisiones trascendentales.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): la limitación es uns entimiento de culpa persistente, el rencor acumulado o juicios internos severos.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): la fuerza bloqueadora es el miedo a cerrar etapas por considerar que el futuro no traerá mejores tiempos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): la fuerza bloqueadora es una constante sensación de incompletitud o frustración acumulada por falta de finales efectivos.\n"
                    continue
        elif i==2:
            res += "TERCERA CARTA: el inconsciente. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): revela una necesidad profunda y no reconocida de libertad y exploración de lo desconocido. Subyace un deseo de soltar ataduras y abandonar la cotidianidad en busca de aventuras. El subconsciente está completamente abierto (y deseoso) de riesgo.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): revela miedo oculto a equivocarse o a perder seguridad. Señala un temor arraigado a lo impredecible y una resistencia a los cambios no planeados que bloquean la espontaneidad.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): revela talentos dormidos y recursos internos que esperan para ser activados. Hay una energía creadora lista para manifestarse aunque aun no se reconozca.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): revela un miedo profundo a no ser suficiente o una tendencia al auto-sabotaje. En el fondo, la psique se considera incapaz de afrontar ciertas situaciones, limitando el uso del talento. Muestra problemas de autoestima subyacentes.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): refleja intuiciones profundas y conocimientos interiorizados e inconscientes que esperan para ser reconocidos. La psique guarda en lo más profundo señales de sueños, símbolos y silencios, que los sentidos físicos pasaron por alto.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): refleja una represión interna de la intuición. Srecretos reprimidos, emociones silenciadas... En el fondo, la psique busca ser escuchada y aceptada.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): muestra un deseo innato de crear, nutrir y experimentar en abundancia. Subyace una energía fértil que quiere dar vida a proyectos y relaciones.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): muestra carencias afectivas ocultas o una sensación de no-merecimiento de las cosas enquistada en lo más profundo de la mente, que regula los comportamientos de forma inconsciente. Puede señalar además miedo al abandono o la esterilidad creativa.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): refleja una necesidad de orden, estructura y seguridad neecsaria para operar, que no son asumidas de forma consciente. Existe un deseo profundo de control y de firmeza. Inconscientemente, tiendes a buscar la seguridad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): refleja temores irracionales y ocultos a la autoridad o al abuso de poder, probablemente causados por algún trauma escondido. Puede transformarse en inseguridad en la propia capacidad de liderazgo.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): revela una necesidad subconsciente de un guía y de pertenencia a una comunidad. Subyace una tendencia a confiar en las tradiciones y un respeto a lo espiritual que no se puede explicar de forma racional.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): revela rechazo oculto a las normas rígidas, rebeldía interiorizada contra estructuras autoritarias, probablemente por traumas internos.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): profundo deseo de conexión absoluta y amor como motor central. Tiende a desarrollar subyacentemente una coherencia entre valores y acciones.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): temores ocultos a la pérdida, al abandono o a la traición. Puede reflejar un conflicto interno entre deseo y deber al que no se presta atención o un carácter altamente indeciso.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): muestra un subconsciente que recibe placer al avanzar, conquistar metas y diigir con firmeza. Impulsos internos de superar pruebas y lograr objetivos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): muestra un miedo irracional al fracaso o a perder el control. Puede señalar una profunda indecisión sobre el sentido de la vida.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): refleja un subconsciente sereno, paciente y con alta tendencia a la compasión. Tendencia a dominar los miedos de forma natural y gran resiliencia interiorizada.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): refleja un subconsciente convulso, con un profundo miedo a perder el control emocional, altas cantidades de ira reprimida o impulsividad.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): revela el deseo inconsciente de soledad, como medio para lograr saber e introspección.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): revela un miedo profundo y no reconocido a la soledad, a la oscuridad interna o al aislamiento forzado.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): muestra un subconsciente altamente adaptable, que asimila los cambios con facilidad. Tiende a presentar una confianza interiorizada en el destino.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): muestra un subconsciente dado al fatalismo o altamente frustrado. Existe una alta disconformidad ante los ciclos. En el fondo, la psique no tolera el cambio y sufre enormemente por repetir errores del pasado.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): reflejo un deseo profundo de alcanzar la verdad. Subyace en el comportamiento la búsqueda de claridad y coherencia con la moral personal. Alta tendencia a la responsabilidad y la rectitud.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): refleja una gran incomodidad interna al ser juzgado o al enfrentar consecuencias. Puede señalar autoengaño o evasión de responsabilidades tan profundas que gobiernan sobre la consciencia.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): subyace un deseo interno de entrega y de transformación que aun no se asume. La psique valora enormemente el sacrificio voluntario.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): puede señalar la avaricia como eje del subconsciente. Sacrificios mal vividos o un sentimiento de estancamiento provocan un temor interiorizado a soltar lo que ya no sirve y al movimiento.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): subyace una necesidad de renacer y de liberarse del pasado. Subconsciente altamente enfocado hacia el futuro.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): subyace un temor arraigado al vacío, por lo que se retiene instintivamente lo que ya no sirve.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): revela un subconsciente centrado en la sensación de armonía. La psique conserva paciencia y capacidad de síntesis de opuestos con extrema facilidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): indica conflictos internos o polaridades sin integrar. Sensación de tensión constante sin que se conozca la causa, lo que da lugar a confusión.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): refleja deseos intensos y temores reprimidos. Subyace un fuerte deseo instintivo por el mundo material, muy difícil de reprimir por la consciencia.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): refleja un subconsciente incapaz de reconocer los aspectos sombríos de la propia personalidad. Esto provoca sensación de incoherencia interna de la que no se encuentra explicación.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): subyace un impulso instinitvo de cambio radical, de ansia por la liberación de uno mismo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): refleja un miedo arraigado a la ruptura, negación de conflictos internos o alto grado de tensión contenida. Puede señalar estructuras rígidas sostenidas por ese temor irracional que gobiernan la consciencia.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): revela un subconsciente con confianza en la vida y en la belleza. Tiende a la esperanza de forma natural.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): revela un subconsciente reacio, cansado y desconfiado. Tiende al cinismo de forma natural.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): muestra un subconsciente con tendencia al caos y a lo simbólico, lo que provoca alto grado de desconexión entre el subconsciente y la consciencia. Alto grado de emocionalidad subyacente e ignorada.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): muestra un subconsciente altamente reprimido e ignorado, generalmente por miedo al torrente de emociones que oculta. Llama a la necesidad de escuchar al mundo interior de forma honesta y objetiva.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): refleja un subconsciente muy optimista. Tiende a la confianza y a la vitalidad de forma instintiva.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): refleja un miedo profundo e irracional al fracaso o a no merecer el éxito que se alcanza, lo que da lugar ba un carácter inseguro y autocrítico que no se puede explicar.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): subyace el deseo por liberarse de cargas pasadas. La psique busca la transformación.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): subyace el miedo a enfrentar los errores del pasado, lo que genera un carácter conservador de forma instintiva y a menudo sentimiento de culpa enquistado.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): revela un subconsciente pleno y sano; en paz con la consciencia. Sin etapas inconclusas ni miedos, sentimientos ni emociones enquistados.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): revela una sensación profunda de incompletitud, de ausencia. Puede indicar asuntos pendientes en el ámbito emocional, originados de la represión consciente.\n"
                    continue
        elif i==3:
            res += "CUARTA CARTA: el objetivo consciente. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): deseo de iniciar un camino nuevo, libre de ataduras y convencionalismos. Buscas vivir con espontaneidad y apertura, confiando en lo inesperado. Tu meta es la aventura y la autenticidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): indica la intención de evitar riesgos o mantener un exceso de precaución. Puede ser el deseo de controlar la incertidumbre y no lanzarse al vacío. La meta consciente es sostener la estabilidad, limitando la espontaneidad.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): representa la meta de manifestar talentos y tomar acciones decisivas. Buscas usar tu creatividad y voluntad para concretar proyectos. El objetivo consciente es dominar los recursos y canalizar el poder personal hacia logros tangibles.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): revela temor a ser manipulado o el intento de controlar más de lo necesario. Puede indicar una meta enfocada en demostrar capacidad sin confianza real. La conciencia persigue eficacia, pero aun desde inseguridad o dudas.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): señala la intención de escuchar a la intuición y conectar con la sabiduría interior. La meta es comprender profundamente, más allá de lo evidente. Buscas claridad espiritual y confianza en tu percepción interna.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): refleja la intención de obtener certezas externas en lugar de confiar en la voz interna. Puede ser un objetivo de racionalizar lo que es intuitivo. La búsqueda consciente es aclarar secretos, aunque con dificultad para confiar.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): representa el deseo de crear, nutrir y experimentar abundancia. La meta es gestar proyectos fértiles o vínculos amorosos plenos. Buscas belleza, creatividad y expresión emocional como camino a la realización.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): indica la intención de resolver carencias afectivas o de alcanzar un sentido de valor propio. Puede señalar deseo de recuperar creatividad bloqueada. La meta es sentirte merecedor de amor y prosperidad.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): simboliza la meta de establecer orden, seguridad y control. Buscas construir estabilidad sólida y ejercer autoridad en tu vida. El propósito consciente es consolidar poder personal y material.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): refleja la intención de liberarse de estructuras rígidas o de resistirse al control externo. Puede ser el deseo de romper con patrones autoritarios. La meta consciente es recuperar autonomía frente a la opresión.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): muestra la búsqueda de guía espiritual, de pertenencia a un grupo o de conexión con los valores tradicionales. La meta es aprender, recibir enseñanza honesta o integrarse en una comunidad que aporte confianza y estructura.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): señala la intención de romper con dogmas o de cuestionar normas establecidas. Puede indicar deseo de un camino personal más auténtico. El objetivo consciente es encontrar libertad espiritual fuera de las reglas tradicionales.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): representa la meta de tomar decisiones alineadas al corazón y de construir un vínculo genuino. Buscas unión, amor y coherencia entre lo que sientes y lo que haces. El propósito es la integración armónica.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): indican la intención de resolver dudas afectivas o superar la indecisión. Puede señalar el deseo de liberarse de dependencias o de reconciliar contradicciones internas. La meta consciente es forjar tu claridad emocional\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): simboliza la meta de avanzar con decisión, conquistar metas y dominar las fuerzas internas. Buscas triunfo, reconocimiento y dirección clara.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): refleja la intención de superar bloqueos en el avance o de recuperar control sobre tu dirección vital. Puede ser un objetivo de disciplinarse o de encontrar el rumbo perdido. La meta es reconducir la energía dispersa.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): representa la meta de dominar los impulsos con paciencia y serenidad. Buscas actuar con compasión, resiliencia y firmeza. El propósito consciente es lograr equilibrio entre instinto y razón.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): refleja la intención de superar inseguridades o falta de autocontrol. Puede señalar la meta de no dejarse llevar por la ira o el miedo. La búsqueda es fortalecer la autoconfianza y recuperar la estabilidad emocional.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): indica la meta de buscar sabiduría interior, retirarse para reflexionar o encontrar el sentido. Buscas claridad a través de la soledad y la introspección. El propósito consciente es hallar respuestas en la propia luz interna.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): refleha el deseo de salir del aislamiento o de recuperar contacto con la sociedad que te rodea. Puede ser un ibjetivo de vencer a la soledad. La meta consciente es equilibrar la introspección con la conexión social.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): simboliza la meta de aprovechar oportunidades, adaptarse al cambio y confiar en la suerte. La persona busca un giro positivo en su vida. El propósito es estar en sintonía con los cambios repentinos y la impredecibilidad de la vida.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): indica el deseo de superar la sensación de estancamiento o mala racha. Puede señalar la meta de recuperar el control sobre lo que se ha vuelto o parece azaroso. La búsqueda consciente es liberarse de la fatalidad achacada a la suerte y tomar iniciativa.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): representa la meta de actuar con rectitud, tomar decisiones objetivas, éticas y equilibradas. Buscas Verdad, Ética y Acción.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): señala la intención de evitar juicios o de resolver injusticias vistas o vividads. Puede ser la meta de reconocer verdades ocultas o aclarar malentendidos que pesan en la conciencia. El objetivo consciente es recuperar el equilibrio y la confiabilidad.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): es el propósito de ver las cosas de formas distintas y aceptar sacrificios por un bien mayor. Buscas comprensión y entrega. La meta consciente es buscar nuevos puntos de vista liberándose de apegos para ganar claridad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): indica la intención de dejar atrás la parálisis o de no realizar sacrificios inútiles. Puede señalar la búsqueda de movimiento y resolución, pero desde una perspectiva más bien cobarde y escéptica ante la efectividad de sus decisiones/sacrificios.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): representa el deseo de transformación y evolución para cerrar ciclos vitales. Buscas renacer y liberarte del pasado de forma pacífica, con el objetivo de avanzar en algún aspecto de tu vida.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): es la intención de superar la resistencia al cambio y de superar los apegos difíciles de soltar. La búsqueda consciente es transitar la transformación inminente con menor temor.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): indica la meta de alcanzar equilibrio, armonía y moderación. Buscas sanar relaciones, integrar opuestos y encontrar paz. El propósito consciente es vivir desde la calma y la coherencia.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): señala el deseo de romper la monoonía y escapar de una vida gris. Buscas experimentar sentimientos y emociones más intensos con el objetivo de enriquecer tu mundo interno en detrimento de la estabilidad y la paz interior.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): refleja el deseo de enfrentar deseos intensos, pasiones o ataduras al mundo material. La persona busca experimentar con lo prohibido o reconocer sus sombras.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): es la intención de liberarse de la dependencia al mundo material, que consideras limitante. La búsqueda consciente es recuperar la autonomía y la autenticidad.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): consiste en la intención de derribar lo falso y permitir cambios radicales. Buscas renovación aunque implique la destrucción absoluta del régimen anterior. La meta es lareconstrucción total de tu vida.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): refleja el deseo de evitar la crisis o de controlar el impacto del cambio inminente. Puede señalar intención de suavizar rupturas. La meta consciente es salvar la estabilidad mientras se transforma lo que se tenga que transformar.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): consiste en la meta de mantener la esperanza, fe o la conexión espiritual. Buscas inspiración, que perdure la ilusión y tienes gran confianza en el futuro. El propósito consciente es mantener viva la ilusión y la confianza sobre la que se sostiene tu estado actual (positivo).\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): refleja la meta de recuperar la fe perdida tras el desencanto. Puede señalar la meta de superar la desesperación que queda tras el deseo, el desánimo o volver a creer en la vida y en ti mismo. La búsqueda consciente es abandonar el pesimismo que ahoga.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): representa la intención de conectar con tus emociones y sentimientos. Sentir más o mejor, sin permitir que te desborden.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): es la intención de aclarar confusiones, callar el torrente emocional o salir de engaños. Puede señalar la meta de recuperar la objetividad. La búsqueda consciente es despejar la niebla emocional y ganar claridad.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): es el deseo de vivir con alegría, éxito y autenticidad. Buscas expandirte, disfrutar del momento y compartir felicidad. La meta consciente es irradiar luz y vitalidad a tus seres queridos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): puede señalar la meta de encontrarse a uno mismo. Suele indicar la intención de superar las inseguridades y brillar con naturalidad.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): muestra la meta de responder a un llamado interno, liberar cargas pasadas y renacer. Urge la resolución de las cuestiones inconclusas y cerrar deudas emocionales. Buscas despertar a una nueva etapa vital de forma plena.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): refleja la intención de superar bloqueos ligados a la culpa o la indecisión. La búsqueda consciente es aceptar los conflictos internos y afrontarlos sin temor.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): representa la meta de alcanzar plenitud, integración y éxito.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): indica la intención de resolver asuntos inconclusos o superar la falta de visión global que produce el estancamiento.\n"
                    continue
        elif i==4:
            res += "QUINTA CARTA: el pasado reciente. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): se emprendió un nuevo camino con entusiasmo, vitalidad e ilusión. Confiaste en lo desconocido y esta energía de aventura aun resuena en el presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): informa de decisiones precipitadas o imprudencias que han generado consecuencias. Pudo haber temeridad o desorganización y esas huellas llegan al presente.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): muestra un momento en el que tomaste la iniciativa para conseguir objetivos. Hubo una chispa de acción creativa que abrió puertas importantes.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): sugiere engaños, manipulaciones o dudas en el uso del propio poder. Hubo intentos fallidos de concretar ideas o proyectos.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): refleja una etapa de introspección, escucha y conexión con el inconsciente. Esta búsqueda interior dejó huellas en tu forma de afrontar el presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): señala un momento de confusión por desconfiar en tus intuiciones o en tus personas más cercanas. Dificultad para llegar a conclusiones verdaderas.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): simboliza un periodo de creatividad y abundancia. Este periodo resultó ser muy nutritivo y embriagador para ti y puede llegar a desencadenar nostalgia.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): sugiere bloqueos creativos o carencias afectivas importantes en el pasado. Sensación de falta de apoyo o de esterilidad.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): muestra un periodo de consolidación de estructuras de poder, normas y estabilidad. Descubrimiento de figuras de autoridad, logros materiales...\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): señala exceso de control sufrido o ejercido, o un posible conflicto con la autoridad imperante que provoca un sentimiento de opresión\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): muestra aprendizaje o un periodo de integración en una comunidad. También puede simbolizar experiencias relacionadas con la tradición y la moral.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): señala un periodo de descubrimiento moral, como una rebelión contra la tradición establecida o ruptura con instituciones.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): reflejan una elección importante en el ámbito afectivo. Hubo unión, decisión o compromiso.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): señala momentos de indecisión, separación o conflicto con tus allegados.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): muestra un logro alcanzado gracias a la determinación propia. Avances y triunfalismo que fortalecieron tu actitud en el presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): sugiere una pérdida de control o un fracaso en algún aspecto vital.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): señala una etapa de superación de obstáculos de forma asertiva o de dominación de impulsos mediante la razón.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): refleja momentos de inseguridad, falta de control propio o de debilidad frente a los desafíos.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): sugiere un periodo de soledad autoimpuesta (directa o idnirectamente), de melancolía o de reflexión profunda. Una etapa bastante gris dominada por el silencio.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): muestra un periodo de aislamiento forzado, o demasiado largo que terminó afectándote negativamente. Puede referirse también a situaciones de evasión o miedo profundo a la soledad.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): simboliza un giro positivo en el pasado, una oportunidad aprovechada o un cambio fruto del azar que resultó ser positivo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): refleja un periodo en el que predomina la sensación de azar en el entorno o de pérdida del control absoluta. Puede reflejar también retrasos u obstáculos.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): señala decisiones justas, acuerdos equilibrados o resolución de asuntos legales.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): indica injusticias, decisiones parciales, subjetivas o engaños que han marcado el camino hacia el presente. También puede identificarse con situaciones de abuso de poder o de crueldad.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): muestra un tiempo de pausa, de calma interna o de espera y entrega a nuevas perspectivas. A menudo, se relaciona con algún tipo de sacrificio realizado en pos de un objetivo que no se termina de alcanzar.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): muestra un periodo de estancamiento inútil, de incapacidad de abandonar perspectivas erróneas o de parálisis total en algún aspecto de tu vida.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): indica una transformación profunda en algún aspecto vital en el pasado cercano, cierre de un ciclo o pérdida significativa.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): refleja periodos de resistencia al cambio en el pasado, negacionismo de algún tipo o la postergación de finales. También puede asociarse a periodos de procrastinación severa.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): muestra un periodo de armonía, paz mental o sanación. Sugiere ausencia de emociones intensas y moderación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): señala conflictos (internos o externos) que vulneraron tu estabilidad, algún tipo de exceso o falta de mesura a la hora de actuar en la etapa anterior.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): refleja un periodo marcado por las pasiones materiales, intensidad, deseos... Ninguno supuso una mejora sustancial de tu estado espiritual.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): indica intentos de enfrentar excesos, manipulaciones y el deseo de superar las limitaciones terrenales que no son capaces de satisfacer el espíritu.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): simboliza un periodo de crisis o ruptura bastante violenta o súbita, de reconstrucción de estructuras o colapso.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): refleja intentos de evitar un cambio drástico, de minimizar una crisis importante o la incapacidad de superar un estancamiento profundo.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): muestra un periodo de renacimiento de esperanza, ilusión y fe en el futuro, momentos radiantes o inspiración.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): indica desilusión, pérdida de confianza en un proyecto o persona o falta de fe. Un periodo oscuro. También puede indicar fenómenos paranormales.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): representa un tiempo de intuición, sueño y conexión con el mundo emocional o espiritual. Podría indicar momentos de emocionalidad intensa o de descubrimiento de sentimientos profundos.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): muestra engaños descubiertos o salidas de periodos de confusión. También puede indicar una etapa de desconexión con tu mundo emocional o que este se encuentra en estado convulso, sin ser comprendido.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): refleja una etapa de éxito, alegría y vitalidad, a menudo suele ser compartida. Un periodo luminoso para ti.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): refleja una etapa de inseguridades, falta de reconocimiento externo por tus logros o una felicidad truncada por algún factor, pérdida del optimismo...\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): muestra una etapa de despertar, de afrontar decisiones importantes, de reconciliación o de cierre de asuntos pendientes con el pasado.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): representa la no aceptación de responsabilidades y culpas pasadas. Un periodo de resistencia a afrontar verdades con valentía que influye altamente en tu presente.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): simboliza un periodo de logros, de culminación exitosa o de habilidad para comprender situaciones en su totalidad. También puede indicar integración plena alcanzada en alguna comunidad o proyecto.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): revela asuntos del pasado inconclusos o metas no alcanzadas. También puede hacer referencia a un periodo de falta de visión o ambición completamente condicionante o a un sentimiento de vacío.\n"
                    continue
        elif i==5:
            res += "SEXTA CARTA: el futuro cercano. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): se emprenderá un nuevo camino con entusiasmo, vitalidad e ilusión. Confiaste en lo desconocido y esta energía de aventura comienza a mostrarse en el presnte.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): informa de decisiones precipitadas o imprudencias que generarán consecuencias. Advierte de la posibilidad de haber temeridad o desorganización.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): muestra un momento en el que tomarás la iniciativa para conseguir objetivos. Habrá una chispa de acción creativa que abrirá puertas importantes.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): sugiere engaños, manipulaciones o dudas en el uso del propio poder. Habrá intentos fallidos de concretar ideas o proyectos.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): refleja una etapa de introspección, escucha y conexión con el inconsciente. Una búsqueda interior que emplearás para afrontar los problemas y adversidades confiando en tu intuición.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): señala un momento de confusión por desconfiar en tus intuiciones o en tus personas más cercanas. Dificultad para llegar a conclusiones verdaderas o un intento de llegar a la verdad de forma ortodoxa y rigurosa.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): simboliza un periodo de creatividad y abundancia. Este periodo resultará ser muy nutritivo y embriagador para ti y puede llegar a desatar el anhelo en el presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): sugiere bloqueos creativos o carencias afectivas importantes en el futuro, o la llegada de las consecuencias que estas han generado. Sensación de falta de apoyo o de esterilidad e improductividad.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): muestra un periodo de consolidación de estructuras de poder, normas y estabilidad. Descubrimiento de figuras de autoridad, logros materiales...\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): señala exceso de control sufrido o ejercido, o un posible conflicto con la autoridad imperante que provocará un sentimiento de opresión. También puede mostrar situaciones de abuso de poder.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): muestra aprendizaje o un periodo de integración en una comunidad. También puede simbolizar experiencias futuras relacionadas con la tradición y la moral.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): señala un periodo de descubrimiento moral en el futuro, como una rebelión contra la tradición establecida o ruptura con instituciones.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): reflejan una elección importante en el ámbito afectivo. Búsqueda de unión, decisión o compromiso.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): señala momentos de indecisión, separación o conflicto con tus allegados.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): muestra un logro alcanzado gracias a la determinación propia. Avances y triunfalismo que fortalecerán tu actitud.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): sugiere una pérdida de control, de voluntad o del rumbo o un fracaso en algún aspecto vital.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): señala una etapa de superación de obstáculos de forma asertiva o de dominación de impulsos mediante la razón.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): refleja momentos de inseguridad, falta de control propio o de debilidad frente a los desafíos.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): sugiere un periodo de soledad autoimpuesta (directa o idnirectamente), de melancolía o de reflexión profunda. Una etapa bastante gris dominada por el silencio.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): muestra un periodo de aislamiento forzado, o demasiado largo, incluso de frialdad, que terminará afectándote negativamente. Puede referirse también a situaciones de evasión o de miedo profundo a la soledad.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): simboliza un giro positivo en el futuro, una oportunidad que debes aprovechar o un cambio azaroso que resultará positivo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): refleja un periodo en el que predomina la sensación de azar en el entorno o de pérdida del control absoluta. Puede reflejar también retrasos u obstáculos.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): señala decisiones justas, acuerdos equilibrados o resolución de asuntos legales en el futuro cercano.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): indica injusticias, decisiones parciales, subjetivas o engaños que surgen de la situación presente. También puede identificarse con situaciones de abuso de poder o crueldad.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): muestra un tiempo de pausa, de calma interna o de espera y entrega a nuevas perspectivas. A menudo, se relaciona con algún tipo de sacrificio que tienes en mente en pos de un objetivo que no se termina de alcanzar.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): muestra un periodo de estancamiento inútil, de incapacidad de abandonar perspectivas erróneas o de parálisis total en algún aspecto de tu vida por culpa de un continuismo feroz.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): indica una transformación profunda en algún aspecto vital en el futuro cercano, cierre de un ciclo inminente pero suave o pérdida significativa.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): refleja periodos de resistencia al cambio en el futuro inminente, negacionismo de algún tipo o la postergación de finales. También puede asociarse a periodos de procrastinación severa.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): muestra un periodo de armonía, paz mental o sanación. Sugiere ausencia de emociones intensas y moderación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): señala conflictos (internos o externos) que vulnerarán tu estabilidad, algún tipo de exceso o falta de mesura a la hora de actuar en la próxima etapa.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): refleja un periodo marcado por las pasiones materiales, intensidad, deseos... Ninguno supondrá una mejora sustancial de tu estado espiritual.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): indica intentos de enfrentar excesos, manipulaciones y el deseo de superar las limitaciones terrenales que no son capaces de satisfacer tu espíritu.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): simboliza un periodo de crisis o ruptura bastante violenta o súbita, de reconstrucción de estructuras o de colapso.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): refleja intentos de evitar un cambio drástico, de minimizar una crisis importante o la incapacidad de superar un estancamiento profundo.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): muestra un periodo de renacimiento de esperanza, ilusión y fe en el futuro, momentos radiantes o inspiración.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): indica desilusión, pérdida de confianza en un proyecto o persona o falta de fe. Un periodo oscuro. También puede indicar fenómenos paranormales inminentes.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): representa un tiempo de intuición, sueño y conexión con el mundo emocional o espiritual. Podría indicar momentos de emocionalidad intensa o de descubrimiento de sentimientos profundos en el futuro cercano.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): muestra engaños que descubrirás o salidas de periodos de confusión. También puede indicar una etapa de desconexión con tu mundo emocional o que este se encontrará en estado convulso, sin ser comprendido.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): refleja una etapa de éxito, alegría y vitalidad, a menudo suele ser compartida. Un periodo luminoso para ti se avecina.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): refleja una etapa de inseguridades, falta de reconocimiento externo por tus logros o una felicidad truncada por algún factor, pérdida del optimismo...\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): muestra una etapa de despertar, de afrontar decisiones importantes, de reconciliación o de cierre de asuntos pendientes con el presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): representa la no aceptación de responsabilidades y culpas que te persiguen. Un periodo de resistencia a afrontar verdades con valentía que influirá mucho en tu comportamiento.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): simboliza un periodo de logros, de culminación exitosa o de habilidad para comprender situaciones en su totalidad. También puede indicar integración plena alcanzada en el futuro en alguna comunidad o proyecto.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): revela asuntos del presente que permanecerán inconclusos o metas no alcanzadas. También puede hacer referencia a un periodo de falta de visión o ambición completamente condicionante o a un sentimiento de vacío.\n"
                    continue
        elif i==6:
            res += "SÉPTIMA CARTA: la personalidad. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): describe a alguien libre, espontáneo y abierto a lo nuevo, que no le teme al riesgo. Una persona curiosa y confiada. Su autenticidad atrae, pero puede dar la impresión de falta de madurez o de rumbo definido.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): describe una tendencia a la imprudencia, la evasión de responsabilidades o la ingenuidad excesiva. Puede señalar a una persona caótica y temeraria. La falta de rumbo puede hacerle perder oportunidades importantes y generar inestabilidad a su alrededor.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): describe a alguien ingenioso, seguro de sí mismo, capaz de transformar ideas en realidad y de manipular situaciones a su favor. Su habilidad para comunicarse y utilizar todos los recursos y habilidades disponibles le permiten destacar en distintos ámbitos. Representa una identidad activa, con iniciativa y carisma natural.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): describe a alguien que duda constantemente de sus capacidades o que es propenso a caer en la manipulación y el engaño. También puede indicar una persona con gran carisma que usa sus talentos de forma egoísta o superficial. Refleja un gran temor a no ser suficiente, lo que bloquea su gran potencial creativo.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): describe una identitdad introvertida, introspectiva, sabia y profunda. Es una persona sutil, con gran intuición y sensibilidad hacia lo oculto. Se percibe como reservada, pero guarda un magnetismo que inspira respeto.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): describe a alguien desconectado con su intuición, que oculta demasiado, dificultando la cercanía con los demás. También se asocia con problemas de confianza o con una frialdad extrema.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): describe a alguien cálido, creativo y fértil en ideas o proyectos. Es una identidad que nutre e inspira a otros, como una figura maternal. Representa sensualidad, carisma y capacidad de generar armonía a su alrededor.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): describe una tendencia a la dependencia emocional, los celos o dificultad para expresar su mundo interior. Indica cierta impulsividad o falta de atención y cuidado que provoca que suelas dejar proyectos inconclusos. Puede mostrar tendencia a la validación externa.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): describe a una persona disciplinada, firme y con gran sentido de la responsabilidad. Inspira respeto y orden a su alrededor y se erige como figura de líder natural a menudo. Representa una identidad algo fría, que se apoya en la lógica, la estabilidad y la autoridad ganada legítimamente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): describe una identidad rígida, autoritaria y con dificultad para empatizar. Puede señalar a alguien controlador, que impone sus ideas. A menudo, alude a inseguridad disfrazada de dureza o a incapacidad de confiar en los demás.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): describe a alguien que respeta las normas por encima de todo, que apoya las tradiciones y el aprendizaje formal. A menudo se percibe como guía o maestro, alguien que transmite conocimiento y valores. La identidad está fuertemente ligada a una corriente ética que apoya firmemente y al compromiso hacia una comunidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): describe a alguien que cuestiona las reglas establecidas y prefiere trazar su propio camino. Una identidad altamente independiente a menudo catalogada como rebelde. A veces, esta actitud te hace inspirador, aunque puede generar conflictos en tu entorno.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): desribe a alguien afectuoso, sociable y altamente empático. Una identidad que valora la unión y la conexión emocional. También muestra una tendencia a la meditación antes de tomar decisiones importantes.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): describe una persona insegura y/o indecisa, con dificultad para compormeterse. Refleja cierta tendencia a depender demasiado de los demás y un temor a equivocarse en el amor y en la vida.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): describe a alguien determinado, ambicioso y con gran capacidad de enfoque. Transmites seguridad y logras tus metas gracias a una voluntad férrea. Representa una identidad dinámica, en constante avance y con fuerteespíritu de conquista.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): describe a alguien disperso, impulsivo o que no es capaz de controlar sus impulsos o deseos. Puede señalar a alguien que se frustra fácilmente ante adversidades e indica riesgo a caer en conductas dominantes o excesivamente competitivas.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): describe una persona serena, paciente y con gran autocontrol. Su energía inspira confianza y transmite seguridad. Representa una identidad que enfrenta desafíos con suavidad y valor, sin necesidad de imponerse agresivamente.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): describe una lucha constante con la inseguridad, la falta de confianza o los arrebatos emocionales. Puede ser alguien que se siente vulnerable y lo esconde con actitudes dominantes o retraídas. Refleja necesidad de aprender a confiar en sí mismo.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): describe a alguien reflexivo, sabio y muy reservado. Es una identidad que busca la verdad dentro de sí misma y tiende a desconectarse del entorno. Transmite calma a los demás, es maduro y valora la soledad como lugar seguro.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): describe una persona con tendencia al aislamiento, miedo al contacto o dificultad para compartir sus experiencias y conocimientos. Puede describir a alguien excesivamente frío y distante, que prefiere observar el mundo en tercera persona antes que arriesgarse a ser herido. Puede indicar una conservación exagerada.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): describe a alguien adaptable, optimista y con gran confianza en la vida. Tu carácter flexible te permite aprovechar oportunidades inesperadas. Es una identidad que fluye con el cambio y que se enriquece con cada giro de la vida.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): describe una tendencia al pesimismo, al inmovilismo y a repetir patrones erróneos. Puede señalar a alguien que se siente víctima del azar y que tiene dificultades para tomar el control efectivo de su situación.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): describe a alguien íntegro, justo y equilibrado. La identidad está marcada por la primacía y la búsqueda de la verdad y un carácter honesto. Inspira confianza y se guía por una ética firme en todas las decisiones.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): describe a alguien que suele caer en la autojustificación, la rigidez o la parcialidad. A veces, tienes dificultad para asumir responsabilidades y se basa en el miedo a la culpa. La identidad puede ser percibida como injusta, egoísta o incoherente.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): describe a una persona original, capaz de ver la vida desde perspectivas poco convencionales. La identidad está marcada por la paciencia y el desapego y se trata de una persona dispuesta a hacer sacrificios en favor de un bien mayor o un crecimiento personal.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): describe una identidad estancada, que se resiste a cambiar de perspectiva y con dificultad para soltar lo que ya no sirve. Puede describir a alguien pasivo, indeciso o que posterga constantemente. También señala la sensación de estar atrapado en un callejón sin salida.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): describe a alguien transformador, que no teme a los finales porque los vive como oportunidades de renovación. La identidad está marcada por la capacidad de reinventarse a sí mismo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): describe a alguien que no acepta los cierres, con gran nostalgia y resistencia a soltar el pasado. Indica dificultad para aceptar la evolución natural de los procesos personales, lo que puede conducir a la melancolía.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): describe a alguien armónico, calmado, paciente y conciliador. La identidad está marcada por unir opuestos y generar paz en su entorno. Inspira confianza, tranquilidad y se erige como punto de unión entre grupos.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): describe a alguien inestable, con dificultad para alcanzar posiciones moderadas en emociones y actitudes. Puede señalar una persona impulsiva o con tendencia a los extremos, lo que complica en gran medida sus relaciones con el exterior.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): describe una persona carismática, amgnética y con fuerte presencia. Bastante egocéntrica, cuya identidad se centra en los deseos y las pasiones profundas. Representa a alguien que vive sin miedo a lo prohibido, con ansia de intensidad y, en muchas ocasiones, fuertemente ligado al mundo material.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): describe una identidad de lucha continua con la dependencia material, temores o apegos internos dañinos. Se asocia a una persona que está en proceso de liberación de cadenas emocionales y materiales y realización personal, en busca de profundidad. La identidad es el fruto del enfrentamiento entre las propias sombras del pasado y el deseo de superación.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): describe a alguien convulso, inestable y sin miedo a provocar cambios drásticos. La identidad está marcada por la autenticidad y la valentía feroz, sin miramientos. A menudo se cataloga como disruptivo y en ocasiones, violento.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): describe a alguien pusilánime, incapaz de superar adevrsidades por su cuenta. Una identidad que teme al cambio y evita todo tipo de confrontaciones, se aferra a lo conocido sacrificando su evolución personal. También refleja la tendencia a acumular tensiones por medio al conflicto hasta que explota.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): describe a una persona inspiradora, optimista e ilusionada, llena de fe en la vida. Transmites serenidad y esperanza a quienes te rodean. La identidad está vinculada a la autenticidad, la creatividad y la confianza en el futuro.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): describe a alguien inseguro, que acumula decepciones que le han hecho perder la fe o la esperanza. La identidad se percibe apagada y tiende a la melancolía extrema. Sueles adoptar posturas cínicas.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): describe a alguien muy sensible, intuitivo y para el que los sentimientos y emociones propios son lo primordial a la hora de conectar consigo mismo y con los demás, lo que provoca cierta tendencia a la egolatría. Es una identidad misteriosa, con gran capacidad artística y que inspira curiosidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): describe a alguien que presenta dificultad para percibir la realidad como es debido a un fuerte subjetivismo, lo que provoca una tendencia al engaño o autoengaño. Señala una identidad algo ansiosa, egoísta y que disfruta de la intensidad emocional.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): describe a alguien alegre, luminoso y generoso. Es una identidad transparente, muy optimista y llena de vitalidad, cuya presencia anima a los demás, aunque a veces puede ser catalogada como cargante. Representa autenticidad y confianza en la vida, con un corazón abierto al mundo.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): describe a alguien bastante inseguro, con gran necesidad de validación externa o tendencia a opacar sus propios logros por no considerarse digno de ellos. Puede señalar una identidad con gran potencial creativo, que teme brillar por miedo al juicio de otros.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): describe a alguien altamente consciente, reflexivo y dispuesto a asumir las responsabilidades que sobre él recaen. Es una identidad que busca la verdad y no teme en enfrentar su pasado para crecer. Suele ser considerado como inspirador por su capacidad de transformación sosegada.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): describe a alguien aterrado de enfrentar sus demonios, que posterga decisiones importantes o que se resiste a sumir la verdad por miedo feroz a la autocrítica y a escuchar al llamado de su conciencia. Una identidad continuista que realmente no desea serlo, lo que provoca sufrimiento.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): describe a alguien pleno, con carácter expansivo y en sintonía con la totalidad. Se percibe como una persona madura, íntegra y confiada, con gran afán de compartir sus logros con el mundo.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): describe una sensación de incompletitud, de metas truncas o de estancamiento por falta de comprensión que genera gran frustración y en ocasiones críticas, rencor. También puede describir personas que no salen de su zona de confort o que posterga cerrar capítulos importantes.\n"
                    continue
        elif i==7:
            res += "OCTAVA CARTA: el entorno. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): muestra un ambiente abierto, en movimiento y lleno de posibilidades inesperadas. Las circunstancias invitan a explorar lo nuevo, a arriesgar y a salir de la rutina. Es un contexto donde reina la frescura y el potencial de comienzos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): muestra un entorno inestable o caótico. Las personas alrededor pueden actuar de manera imprevisible o irresponsable, generando inseguridad en ti. Este ambiente dificulta la claridad y puede desviarte de tus objetivos.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): muestra un contexto rico en recursos, creatividad y oportunidades para materializar tus proyectos. Las personas alrededor favorecen la acción y la comunicación. Todo invita a emplear tus talentos y habilidades para generar resultados.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): muestra manipulación, superficialidad o falta de confianza. Puede hacer referencia a personas que ocultan intenciones o un ambiente donde lo prometido no se cumple. La energía externa puede empujar a la desconfianza y al autoengaño.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): muestra un ambiente introspectivo, cargado de intuición y calmado. Las personas de alrededor tienden a guardar secretos o actuar con prudencia. Prevalece lo oculto y lo sutil sobre lo evidente y te invita a prestar mucha atención.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): muestra confusión, falta de claridad o secretos que bloquean la comunicación efectiva. Las personas alrededor pueden actuar de manera excesivamente reservada, generando dudas sobre las verdaderas intenciones.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): muestra abundancia, fertilidad y un ambiente de crecimiento. El entorno favorece la creación y gestación de ideas, realciones y proyectos. Las personas de alrededor ofrecen apoyo, cuidado y empatía.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): muestra estancamiento, falta de apoyo o ambientes estériles, en los que no se puede crear nada. Puede señalar bloqueos en proyectos o relaciones sofocantes. Las personas alrededor pueden mostrar celos o actitudes posesivas.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): muestra un entorno estable y bien estructurado. El ambiente está regido por unas normas y roles claros que proporcionan orden. Las personas de alrededor ofrecen apoyo desde la disciplina y la organización.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): muestra rigidez, control excesivo o un sistema de abuso de poder. Puede señalar un ambiente autoritario, donde las reglas pesan más que las necesidades. También puede hacer referencia a problemas por falta de flexibilidad.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): muestra un contexto tradicional, fundamentado en creencias o valores compartidos. Tienden a ser entornos jerarquizados, donde se apoya el aprendizaje dentro del marco ético imperante y la integración en la comunidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): muestra rebeldía, falta de coherencia o rechazo a la autoridad establecida. Puede indicar un ambiente con el que no estas conforme de forma activa o un entorno hostil hacia tus creencias y valores.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): muestra un ambiente afectuoso, cooperativo y basado en la unidad. Las personas de alrededor favorecen las relaciones, las decisiones colectivas y el entendimiento mutuo. Es un contexto donde reinan la armonía y la empatía.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): muestra confusión, división e indecisión. Puede señalar ambientes marcados por conflictos emocionales o por falta de consenso prolongada. Las personas de alrededor meustran actitudes conflictivas, dudas o dificultades para llegar a acuerdos.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): muestra un ambiente dinámico, lleno d emovimiento y oportunidades de mejora. Las personas de alrededor favorecen la acción y la determinación. Es un contexto que invita a conquistar metas y a superar obstáculos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): muestra desorden, rivalidades o falta de dirección. Puede señalar ambientes donde las personas avanzan en distintas direcciones, dificultando el progreso conjunto. Puede hacer referencia a personas impacientes, con exceso de competitividad o actitudes exageradamente pasivas.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): muestra un ambiente de armonía y estabilidad, cargado de calma. Las personas ofrecen apoyo paciente y actitudes conciliadoras. Invita a la serenidad y al dominio de impulsos mediante la razón. Se trata de un entorno de contención emocional sana.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): muestra tensiones, falta de autocontrol en las personas y conflictos. Es un ambiente donde predominan los impulsos desmedidos, las reacciones exageradas y las personas de alrededor pueden transmitir ansiedad u hostilidad.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): muestra un ambiente reflexivo y silencioso, orientado al aprendizaje profundo obtenido mediante la meditación individual. Es un ambiente bastante neutro que puede provocar sentimiento de soledad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): muestra un ambiente que te obliga a la soledad forzada, las personas se muestran cerradas y frías. Es un entorno muy poco comunicativo y represivo por medio del silencio helado y la falta de conexión.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): muestra un ambiente cambiante, lleno de oportunidades inesperadas. Las personas de alrededor traen movimiento y giros. Es un contexto en el que las transformaciones inesperadas ocurren y puede producir sensación de personas unidas por el efecto del azar.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): muestra inestabilidad y repeticiones de ciclos no enriquecedores. Puede haber bloqueos por falta de direccionalidad, que impiden el progreso colectivo, sensación de estancamiento por exceso de individualismo. El ambiente destruye toda sensación de control que posees y obliga a aceptar lo imprevisto.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): muestra un ambiente transparente, guiado por normas claras asimiladas por todos. La ética tiene un papel fundamental en tus relaciones interpersonales. Es un contexto que favorece acuerdos justos y decisiones responsables hacia las personas ajenas.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): muestra falta de honestidad o arbitrariedad moral en el ambiente. Puede señalar entornos sin una ética clara, donde imperan las morales individuales. Puede haber juicios erróneos o injusticias y las personas de alrededor pueden mostrar parcialidad o doble moral en sus relaciones interpersonales.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): muestra un ambiente de pausa, reflexión y necesidad de análisis desde diversas perspectivas. El entorno se caracteriza por la inactividad y el desapego. Es un contexto que favorece la espera y el análisis exhaustivo en detrimento de la acción.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): muestra un ambiente continuista por incapacidad de análisis efectivo. Inactividad excesiva de los agentes externos a ti. El contexto puede generar sensación de sacrificios inútiles.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): muestra un ambiente de cambio. Sugiere cierres importantes en etapas de relaciones interpersonales para comenzar nuevas etapas en ella. Sugiere un entorno en transformación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): muestra un entorno con el que ya no estás cómodo por ausencia de cambio. Un ambiente que se resiste al cambio natural que traen los procesos de la vida. Costumbrismo en las relaciones interpersonales que obstaculizan la evolución.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): muestra un ambiente de equilibrio y conciliación. Las personas de alrededor aportan serenidad, paciencia y cooperación. Es un contexto que favorece la sanación progresiva y la moderación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): muestra desequilibrios en las relaciones con los demás, unas partes dan más que otras. Sugiere tensiones y desajustes en el entorno, conflictos consecutivos por incompatibilidad de personalidades, dificultad para alcanzar acuerdos intermedios o tendencia al extremismo en tus alrededores.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): muestra un ambiente intenso, fundamentado en los lazos terrenales (pasiones, deseos, tentaciones...). Puede señalar personas magnéticas, carismáticas y muy influyentes. Es un contexto que favorece el materialismo, la dependencia y la superficialidad subyacente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): muestra un ambiente de sanación. Es un contexto de liberación, donde se tratan de romper cadenas de control y apegos tóxicos con el objetivo de una mayor profundidad en tus relaciones. Invita a la recuperación de autonomía.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): muestra un ambiente de cambio abruptos y violentos, revelaciones y sacudidas continuas. Puede señalar a personas altamente inestables, con gran capacidad destructiva y con gran influencia en ti, aunque también puede indicar un entorno que colapsa hasta sus cimientos porque se volvió insostenible, y abrirá paso a uno más auténtico.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): muestra un entorno incapaz de superar el estancamiento, en el que las personas se aferran a lo conocido. Puede señalar tensiones acumuladas que esperan a explotar.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): muestra un entorno de esperanza, inspiración e ilusión. Las personas de alrededor transmiten apoyo, optimismo y confianza en el futuro. Un entorno que invita a la creatividad y a compartir sueños y esperanzas conjuntas.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): muestra un ambiente cargado de desilusión y pérdida de confianza. Puede señalar a personas que transmiten dudas o gran pesimismo o a rencores no resueltos.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): muestra un ambiente cambiante, complejo y lleno de matices. Puede indicar que los lazos que te unen a las personas tienen carácter emocional o sentimental, lo que provoca relaciones más convulsas y situaciones que han de ser estudiadas desde la intuición.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): muestra confusión o una percepción errónea del entorno. Puede referirse a engaños de otras personas, situaciones pocos claras y una tendencia a fluir emocionalmente en las relaciones interpersonales.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): muestra un ambiente de alegría y optimismo que invita a sacar tu expresión más auténtica. Fuerte sentimiento de apoyo desde el exterior, favoreciendo la confianza y el éxito compartido y celebrado.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): muestra un ambiente donde reina la inseguridad o el temor al juicio. Puede señalar a personas que menosprecian los logros ajenos o transmiten envidia. El contexto genera dudas y provoca la retracción individual.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): muestra decisiones pendientes de importancia referidas a ciertas relaciones interpersonales. Exige clarificación, toma de responsabilidad y apertura al cambio en tu forma de interactuar con el exterior.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): muestra un ambiente estancado, fruto del temor a la transformación, a la comunicación y de evitar mirar a la verdad. Puede señalar a personas que se resisten a asumir errores. Inmovilismo.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): muestra un ambiente pleno, de logros compartidos. Un entorno de apertura, integración y celebración. Se favorece la conexión entre individuos afines.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): muestra un ambiente incompleto, donde los procesos de interacción parecen inconclusos. Puede señalar a personas que se niegan a cerrar etapas o a la incapacidad de culminar una relación por determinadas carencias.\n"
                    continue
        elif i==8:
            res += "NOVENA CARTA: esperanzas y miedos. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): refleja el anhelo de libertad, de atreverse a lo desconocido y de iniciar una nueva etapa sin cargas. Como miedo, implica temor a lo incierto, a perder estabilidad o a actuar sin rumbo. Representa la dualidad entre la valentía y la inseguridad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): refleja la esperanza de soltar ataduras y liberarse de influencias caóticas. Como miedo, simboliza temor a caer en la imprudencia, a ser juzgado por irresponsabilidad o a cometer errores por impulsividad. Es la tensión entre soltar carga y perderse por soltar demasiado.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): refleja, como esperanza, la confianza en los propios talentos, deseo de aprovechar oportunidades y de poseer capacidad creativa. Como miedo, implica inseguridad sobre no estar a la altura o temor a que los recursos y habilidades no sean suficientes. Es la dualidad entre la expectativa y la incapacidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): refleja la esperanza de desenmascarar engaños y de dejar atrás conductas manipulativas. Como miedo, simboliza el temor a ser utilizado, engañado o incapaz de materializar ideas. Surge la tensión entre lo auténtico y lo falso.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): refleja el deseo de sabiduría, de conectar con la voz interna de la intuición y de ser capaz de descubrir lo oculto. Como miedo, representa la angustia ante lo desconocido, el silencio o la pasividad. Es el conflicto entre revelación y confusión.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): refleja la esperanza de ser capaz de obtener conocimiento objetivo y verdadero. Como miedo, simboliza la desconfianza, engaños o bloqueos internos que nublen el juicio. Es la lucha entre certeza e incertidumbre.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): refleja el deseo de abundancia, creatividad o fertilidad. Como miedo, refleja temor a perder la prosperidad, a caer en la esterilidad o a no sentirse valorado. Representa la dualidad entre la fertilidad y la esterilidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): refleja la intención de superar bloqueos creativos o el desarrollo de una mayor empatía. Como miedo, es el temor a la dependencia o al estancamiento. Es el contraste entre florecer y quedarse vacío.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): refleja la aspiración de construir estabilidad, orden y seguridad. Como miedo, implica temor a quedarse atrapado en estructuras demasiado rígidas o a perder libertad bajo el peso de la responsabilidad. Representa la tensión entre solidez y rigidez.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): refleja el deseo de liberarse de figuras autoritarias y de recuperar el control propio. Como miedo, consiste en el temor a la falta de disciplina, al caos o a no tener bases firmes sobre las que construir. Indica la dualidad entre romper cadenas opresivas y la falta de sostén.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): refleja, como esperanza, la búsqueda de un guía y sentido espiritual/moral. Como miedo, expresa temor a caer en el conformismo, a seguir normas rígidas sin discutirlas o a perder autonomía. Es la tensión entre la fe en lo establecido y el miedo a la obediencia ciega.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): refleja el deseo de rebelarse contra las normas establecidas y encontrar un camino propio. Como miedo, muestra temor a la exclusión, a no encajar o a perder espiritualidad. Aquí se contraponen la liberación y la soledad.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): refleja el deseo de unión, amor y decisiones correctas a nivel sentimental. Como miedo, simboliza el temor a equivocarse en el ámbito interpersonal o a perder una relación importante. Habla del anhelo de amar frente al miedo a errar y herir.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): refleja unas ganas de salir de la indecisión y lograr claridad. Como miedo, expresa temor a la ruptura, a la traición o a la falta de juicio propio. Se trata del contraste entre la esperanza de valentía y el miedo al dolor.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): refleja el deseo de avanzar, conquistar metas y mantener el control de tu situación. Como miedo, señala el temor a fracasar en el intento o a no tener la voluntad suficiente. Representa la dualidad entre el éxito y el fracaso.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): refleja el anhelo de superar los obstáculos que se presentan y recuperar el rumbo. Como miedo, es el temor a conflictos o rivales difíciles de vencer. Indica la pugna entre el avance y el obstáculo.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): refleja el deseo de controlar los impulsos, actuar con serenidad y superar pruebas con paciencia. Como miedo, expresa el temor a la debilidad interna o no poseer la suficiente resistencia. Es el enfrentamiento entre fortaleza y debilidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): refleja el anhelo de liberarse de la ira y la fachada de dureza y recuperar la paz. Como miedo, es el temor a la vulnerabilidad y a los ataques externos. Representa la lucha entre la falsa fortaleza y la vulnerabilidad.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): refleja el deseo de encontrar respuestas internas, sabiduría y paz en soledad. Como miedo, expresa temor al aislamiento, a la frialdad o a quedar excluído del mundo. Es la lucha entre la introspección y la soledad no deseada.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): refleja las ganas de no sentirte solo, de abandonar el aislamiento y volver a conectar con el mundo exterior. Como miedo, muestra el temor a la ceguera espiritual o al abandono de la personalidad propia. Enfrenta las ganas de conexión con el temor a perder tu esencia.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): refleja, como esperanza, la fe en un futuro mejor y en la buena suerte venidera. Como miedo, expresa temor a la inestabilidad, a los giros inesperados o a perder lo logrado. Es la dualidad de confiar en el destino frente al temor a lo incierto.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): refleja las ganas de romper ciclos y escapar al azar, tomando control. Como miedo, simboliza temor a que todo se repita y a no aprender de los errores. Representa la pugna entre avanzar y estancarse.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): refleja el anhelo de claridad, equilibrio y tomar decisiones justas. Como miedo, es el temor a juicios erróneos y a verdades incómodas. Es la tensión entre la transparencia y el castigo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): refleja el anhelo de superar injusticias vividas o de alcanzar la verdad. Como miedo, simboliza temor a la corrupción y la inmoralidad (sufrirla o ejercerla). Habla del equilibrio entre la reparación y el abuso.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): refleja el deseo de alcanzar los objetivos en mente mediante los sacrificios realizados y la paciencia. Como miedo, se trata del temor a perder el tiempo o a sacrificarse en vano. Es la tensión entre entrega y los sacrificios inútiles.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): refleja, como esperanza, la intención de liberrase de bloqueos y ser capaz de avanzar tras una larga pausa. Como miedo, es el temor a quedar atrapado en la inmovilidad por ser incapaz de obtener nuevas perspectivas. Habla del conflicto entre la esperanza de progreso y el miedo a la falta de visión.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): refleja el deseo de transformarse, cerrar ciclos y renacer. Como miedo, expresa el temor al cambio drástico, a las pérdidas o a lo desconocido. Es la fe en la renovación frente al miedo a lo irreversible.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): refleja el anhelo de superar apegos y abrirse a lo nuevo con valor. Como miedo, es el temor a no poder soltar el pasado y resistirse al cambio necesario. Representa la lucha entre fluir y aferrarse.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): refleja el deseo de equilibrio, armonía y sanación. Como miedo, expresa temor al descontrol, al conflicto o a la imposibilidad de hallar la paz. Es la tensión entre serenidad y discordia.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): refleja como esperanza la búsqueda de superar excesos y desajustes. Como miedo, habla del temor a no poder equilibrar las cosas o a caer en extremos. Representa el conflicto entre la moderación y el extremismo.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): refleja el deseo de disfrutar intensamente de los placeres del mundo, de la pasión y del poder de atracción. Como miedo, expresa temor a la dependencia, a adicciones o al control. Es la lucha entre el placer y el exceso destructivo.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): refleja el anhelo de liberarse de las cadenas, dependencias o tentaciones dañinas. Como miedo, expresa temor a las recaídas, a no lograr liberarse del mundo material... Trata la tensión entre libertad real y recaída.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): refleja la esperanza de derribar abruptamente estructuras inservibles para poder comenzar de nuevo. Como miedo, indica temor al colapso súbito, a la pérdida repentina o a lo inesperado. Habla de la desesperación por renovación frente al miedo al derrumbe.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): refleja las gamas de evitar la destrucción y de suavizar cambios radicales. Como miedo, simboliza temor a prolongar lo inevitable y con ello, el sufrimiento. Representa la lucha entre evitar el sufrimiento o prolongarlo con las propias acciones.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): refleja, como esperanza, la fe en el futuro, anhelo de confianza. Como miedo, implica temor a perder la fe y caer en la desesperanza. Es la búsqueda de fe frente a la desilusión.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): refleja el anhelo de recuperar la confianza perdida y superar la desesperación. Como miedo, simboliza temor a la decepción o al desencanto. Es la pugna entre el anhelo de esperanza y el miedo a la decepción.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): refleja el deseo de conectar con las emociones y ser capaz de comprenderlas y manejarlas. Como miedo, es el temor a dejarse llevar por las emcoiones y perder completamente la dirección o el control. Representa la dualidad entre necesidad de conexión interna y el miedo al desborde.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): refleja las ganas de ser capaz de disipar dudas y percibir la realidad de forma objetiva. Como miedo, representa el temor a la manipulación, la subjetividad exacerbada que te manitiene atrapado en fantasías o a la mentira. Se trata del contraste entre descubrir y engañarse.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): refleja el anhelo de alegría, de éxito y de vínculos positivos. Como miedo, expresa temor a perder la luz interior, al fracaso o a la falta de reconocimiento. Habla de la pugna entre celebrar la vitalidad y el miedo a perderla.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): refleja el deseo de superar las inseguridades y recuperar la confianza en ti mismo. Como miedo, trata el temor a sentir envidia o a no poder brillar con autenticidad. Consiste en la dualidad entre la admiración y la envidia.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): refleja el deseo de ser capaz de afrontar las cuentas pendientes del pasado para poder renacer. Como miedo, es el temor a ser juzgado y a la culpa. Representa la responsabilidad frente a la culpa.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): refleja el anhelo de romper bloqueos y dejar atrás cargas viejas. Como miedo, trata el temor a la parálisis, a perder la oprotunidad de transformarte o a repetir el pasado. Es la tensión entre evolucionar y quedarse atrás.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): refleja el anhelo de plenitud, realización y culminación de logros. Como miedo, simboliza el temor a no alcanzar la totalidad y a dejar ciclos abiertos. Es la búsquedad de totalidad frente al miedo a la incompletitud.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): refleja el deseo de ser capaz de lograr una visión global de las situaciones, que te permitan comprenderlas en su totalidad. Como miedo, simboliza el temor a ser incapaz de descentrar el problema y adquirir un esquema global, conduciendo a la incompletitud. Representa el conflicto entre la capacidad de visión y la obstinación.\n"
                    continue
        elif i==9:
            res += "DÉCIMA CARTA: tendencia del desenlace. \n"
            if tirada[i]==0:
                if orient[i]=='d':
                    res += "EL LOCO (derecho): sugiere un inicio inesperado, un salto de fe hacie nuevas posibilidades y una apertura hacia lo desconocido. Marca una etapa fresca, libre de cargas, aunque con cierta incertidumbre. Se inclina hacia la aventura más que hacia la seguridad.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL LOCO (revés): sugiere un desenlace caótico, con decisiones precipitadas o mal calculadas. Puede implicar pérdidas de dirección, riesgo de imprudencias o falta de preparación. Predice inestabilidad que puede retrasar o desviar los planes originales.\n"
                    continue
            elif tirada[i]==1:
                if orient[i]=='d':
                    res += "EL MAGO (derecho): sugiere un cierre con iniciativa, habilidad y creatividad. Las acciones bien dirigidas se concretan y hay dominio sobre la situación. El futuro se construye con determinación y confianza en los recursos propios.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MAGO (revés): sugiere un desenlace con bloqueos, engaños o pérdida de poder personal. Pueden surgir manipulaciones, malentendidos o proyectos que no se materializan. Llama la atención para recuperar enfoque, confianza en las capacidades propias y autenticidad.\n"
                    continue
            elif tirada[i]==2:
                if orient[i]=='d':
                    res += "LA SUMA SACERDOTISA (derecho): sugiere un desenlace calmado, con tendencia a la comprensión profunda de la situación. Predice un final más introspectivo y sereno que activo.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA SUMA SACERDOTISA (revés): sugiere un desenlace con secretos aun ocultos, bloqueos emocionales o desconexión con la intuición. Puede traer confusión, silencios o dudas sin resolver. Predice inconclusión o falta de transparencia.\n"
                    continue
            elif tirada[i]==3:
                if orient[i]=='d':
                    res += "LA EMPERATRIZ (derecho): sugiere fertilidad y abundancia. Resultados visibles y florecimiento de los proyectos e ideas.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA EMPERATRIZ (revés): sugiere un final estancado, con bloqueos creativos, falta de crecimiento o dependencia. Apremia a reconectar con tu energía de creación.\n"
                    continue
            elif tirada[i]==4:
                if orient[i]=='d':
                    res += "EL EMPERADOR (derecho): sugiere un desenlace sólido, en el que predomina la estabilidad. Los logros se alcanzan mediante la disciplina y el trabajo duro. El resultado obtenido es seguro, pero puede sentirse algo rígido.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL EMPERADOR (revés): sugiere un desenlace de descontrol, rigidez extrema o lucha contra el poder imperante. Puede faltar una estructura que dirija los esfuerzos o caer en imposiciones externas que generan gran sentimiento de resistencia. No hay consolidación firme del cierre.\n"
                    continue
            elif tirada[i]==5:
                if orient[i]=='d':
                    res += "EL SACERDOTE (derecho): sugiere consolidación a través de la tradición, los valores y la guía espiritual. Los resultados se alinean con lo correcto y aceptado socialmente. Se encuentra gran apoyo en una comunidad o en la fe.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SACERDOTE (revés): sugiere un desenlace de rebeldía, de ruptura con las normas o de falta de dirección moral en tus decisiones. Puede haber aprendizaje fuera de lo convencional, pero con riesgo de desorientación y de exclusión.\n"
                    continue
            elif tirada[i]==6:
                if orient[i]=='d':
                    res += "LOS ENAMORADOS (derecho): sugiere un desenlace de decisiones importantes o de unión con otras personas. El resultado viene acompañado de amor, acuerdos o alianzas. Se marca el cierre desde la conciencia.\n"
                    continue
                elif orient[i]=='r':
                    res += "LOS ENAMORADOS (revés): sugiere un final de indecisión, rupturas o equivocaciones. Pueden surgir conflictos en vínculos o decisiones mal tomadas.\n"
                    continue
            elif tirada[i]==7:
                if orient[i]=='d':
                    res += "EL CARRO (derecho): sugiere un desenlace exitoso, de conquistas y logros gracias al esfuerzo y al control. Se alcanza la meta deseada con dirección clara. El resultado es una victoria emergente de la disciplina.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL CARRO (revés): sugiere fracasos o pérdida de rumbo. Pueden presentarse obstáculos, choques de voluntades o falta de control sobre el curso de los hechos. El cierre queda desviado de lo esperado.\n"
                    continue
            elif tirada[i]==8:
                if orient[i]=='d':
                    res += "LA FUERZA (derecho): sugiere un desenlace en calma, nada convulso; con autocontrol y resistencia ante los desafíos. El resultado se obtiene gracias al predominio de la razón sobre las emociones y a la paciencia. Sentimiento de superación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA FUERZA (revés): sugiere un final con tensiones, impulsos descontrolados o debilidad. Pueden presentarse dificultades para mantener la serenidad o para enfrentar los obstáculos. Predice vulnerabilidad.\n"
                    continue
            elif tirada[i]==9:
                if orient[i]=='d':
                    res += "EL ERMITAÑO (derecho): sugiere un desenlace altamente introspectivo, con sabiduría que solo se obtendrá tras un proceso de reflexión profunda. El resultado será la claridad espiritual y la madurez.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL ERMITAÑO (revés): sugiere un final de aislamiento excesivo (autoimpuesto o no) e incomunicación. Puede faltar propósito, ambición o prevalecer un sentimiento de vacío. No se logra la claridad que se buscaba.\n"
                    continue
            elif tirada[i]==10:
                if orient[i]=='d':
                    res += "LA RUEDA DE LA FORTUNA (derecho): sugiere un desenlace dinámico, con cambios positivos y giros inesperados favorables. El cierre queda en manos del azar, con oportunidades que deberás aprovechar para que el resultado sea el esperado.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA RUEDA DE LA FORTUNA (revés): sugiere un desenlace inestable, con repetición de patrones negativos o bloqueos en el progreso. Los giros del azar no favorecen el resultado que esperas y pueden traer demoras. El final se percibe como un ciclo aún inconcluso.\n"
                    continue
            elif tirada[i]==11:
                if orient[i]=='d':
                    res += "LA JUSTICIA (derecho): sugiere un desenlace equilibrado, justo y claro. Las situaciones pendientes se resuelven con diligencia, transparencia y responsabilidad. El resultado trae consecuencias proporcionales a lo actuado.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA JUSTICIA (revés): sugiere un final que se percibe como injusto; con engaños o medias verdades. Puede haber resoluciones parciales, desfavorables o inmorales. Predice un cierre poco honesto y advierte de la importancia de la ética.\n"
                    continue
            elif tirada[i]==12:
                if orient[i]=='d':
                    res += "EL COLGADO (derecho): sugiere un desenlace de entrega, comprensión y nuevos puntos de vista. Predice la necesidad de sacrificios conscientes y de paciencia e invita a la aceptación.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL COLGADO (revés): sugiere un final bloqueado, con incapacidad para actuar, sacrificios inútiles o resistencia al cambio por falta de perspectiva. Predice inmovilismo.\n"
                    continue
            elif tirada[i]==13:
                if orient[i]=='d':
                    res += "LA MUERTE (derecho): sugiere un desenlace de transformación profunda, cierre de ciclo y renacimiento, pero no violentos. El final trae limpieza y un nuevo comienzo. Predice una gran energía de renovación.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA MUERTE (revés): sugiere un final de resistencia al cambio provocado por los procesos naturales, lo que dará lugar a un estancamiento y a la falta de desarrollo personal. Se impide la evolución.\n"
                    continue
            elif tirada[i]==14:
                if orient[i]=='d':
                    res += "LA TEMPLANZA (derecho): sugiere un desenlace armónico, con acuerdos y reconciliación. El resultado fluye en calma y favorece la integración de opuestos. Predice paz y serenidad.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TEMPLANZA (revés): sugiere tensiones, falta de equilibrio o rupturas. Predice confusión y desajustes internos.\n"
                    continue
            elif tirada[i]==15:
                if orient[i]=='d':
                    res += "EL DIABLO (derecho): sugiere un final dominado por pasiones y deseos. Puede haber satisfacción momentánea, pero entraña un alto riesgo de dependencia y superficialidad. Predice materialismo y razonamientos instintivos.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL DIABLO (revés): sugiere una liberación de las limitaciones terrenales o una superación de miedos o adicciones. Predice una independencia y libertad alcanzadas con gran esfuerzo y un corte con lo dañino.\n"
                    continue
            elif tirada[i]==16:
                if orient[i]=='d':
                    res += "LA TORRE (derecho): sugiere un desenlace abrupto y en casos extremos, violentos. Cambios drásticos que pueden llevar a la destrucción de todas las estructuras del presente.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA TORRE (revés): sugiere un desenlace de estancamiento absoluto. Predice un final prolongado, en el que se urge a la transformación. La incapacidad de evolucionar posponde el desenlace real.\n"
                    continue
            elif tirada[i]==17:
                if orient[i]=='d':
                    res += "LA ESTRELLA (derecho): sugiere un desenlace esperanzador, lleno de ilusión y confianza renovada. Predice paz, confianza en el futuro y un optimismo intenso.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA ESTRELLA (revés): sugiere un desenlace de desilusión, de pérdida de la fe o la confianza. Predice un gran desánimo o proyectos frustrados. El final se percibe gris y apagado.\n"
                    continue
            elif tirada[i]==18:
                if orient[i]=='d':
                    res += "LA LUNA (derecho): sugiere un desenlace misterioso, en el que toman gran importancia las intuiciones y las emociones. Puede haber ilusiones o incertidumbres que no permiten claridad total. El final queda abierto a interpretaciones.\n"
                    continue
                elif orient[i]=='r':
                    res += "LA LUNA (revés): sugiere un final convulso, de desconexión emocional absoluta o de torrente de emociones descontrolado.\n"
                    continue
            elif tirada[i]==19:
                if orient[i]=='d':
                    res += "EL SOL (derecho): sugiere un desenlace de alegría, éxito y logros visibles. Predice vínculos felices, vitalidad... ¡Todo perfecto!\n"
                    continue
                elif orient[i]=='r':
                    res += "EL SOL (revés): sugiere un final con pequeñas decepciones, retrasos o falta de confianza. Aunque no es totalmente negativo, el brillo esperado se atenúa. El cierre queda algo opacado.\n"
                    continue
            elif tirada[i]==20:
                if orient[i]=='d':
                    res += "EL JUICIO (derecho): sugiere un desenlace de renacimiento, sanación y liberación del pasado. Predice claridad, perdón y nuevas oportunidades. También suele venir acompañado de un cierre de ciclo de forma consciente.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL JUICIO (revés): sugiere un final marcado por la incapacidad de asumir la culpa de los errores del pasado o de tomar las decisiones necesarias. Una falta de resolución que solo genera incertidumbre.\n"
                    continue
            elif tirada[i]==21:
                if orient[i]=='d':
                    res += "EL MUNDO (derecho): sugiere un desenlace de plenitud, cierre exitoso y logros culminados. Predice triunfo.\n"
                    continue
                elif orient[i]=='r':
                    res += "EL MUNDO (revés): sugiere un final incompleto, con asuntos pendientes o ciclos que no terminan. Puede haber sensación de estancamiento o de éxito parcial. El final necesita de más esfuerzo y ajustes para completarse.\n"
                    continue
    return res