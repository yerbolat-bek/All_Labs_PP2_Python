import pygame 

WIDTH, HEIGHT = 1200, 800  # Ойын терезесінің енін және биіктігін анықтайды.
FPS = 90  # Экранның жаңарту жылдамдығы
draw = False   # Экранда сурет салу қажет екенін көрсетеді
radius = 2    # Қаламның радиусы
color = 'blue'           
mode = 'pen'                 

pygame.init() 
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # Белгіленген өлшемдермен терезе жасайды
pygame.display.set_caption('Paint')  # Терезенің атын орнатады
clock = pygame.time.Clock()  # Уақытты басқару үшін
screen.fill(pygame.Color('white'))  # Экранды ақ түспен толтырады.
font = pygame.font.SysFont('None', 60)  # Мәтінді көрсету үшін қаріп жасайды

def drawLine(screen, start, end, width, color): 
    # Бастапқы және соңғы нүктелердің x және y координаттарын алу
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    # x және y координаттарының абсолюттік айырмашылықтарын есептеу
    dx = abs(x1 - x2) 
    dy = abs(y1 - y2) 
    
    # Тік бұрышты теңдеудің коэффициенттері Ax + By + C = 0
    A = y2 - y1  # Тік бағытта
    B = x1 - x2  # Горизонталь бағытта
    C = x2 * y1 - x1 * y2 
    
    # Егер сызық көлденең болса
    if dx > dy: 
        # x1-ді x2-ден солға қою
        if x1 > x2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # x координаттары бойынша цикл
        for x in range(x1, x2): 
            # Сызық теңдеуін қолдана отырып, y координатасын есептеу
            y = (-C - A * x) / B 
            # (x, y) орнында шеңбер (пиксель) салу
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width) 
    # Егер сызық тік болса
    else: 
        # y1-ді y2-ден төмен қою
        if y1 > y2: 
            x1, x2 = x2, x1 
            y1, y2 = y2, y1 
        # y координаттары бойынша цикл
        for y in range(y1, y2): 
            # Сызық теңдеуін қолдана отырып, x координатасын есептеу
            x = (-C - B * y) / A 
            # (x, y) орнында шеңбер (пиксель) салу
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)

def drawCircle(screen, start, end, width, color): 
    # Бастапқы және соңғы нүктелердің x және y координаттарын алу
    x1 = start[0]  # Бастапқы нүктенің x координатасын алу
    x2 = end[0]  # Соңғы нүктенің x координатасын алу
    y1 = start[1]  # Бастапқы нүктенің y координатасын алу
    y2 = end[1]  # Соңғы нүктенің y координатасын алу
    
    # Шеңбердің ортасын есептеу
    x = (x1 + x2) / 2  # Шеңбердің ортасы бойынша x координатасын есептеу
    y = (y1 + y2) / 2  # Шеңбердің ортасы бойынша y координатасын есептеу
    
    # Шеңбердің радиусын есептеу
    radius = abs(x1 - x2) / 2  # Шеңбердің радиусын есептеу
    
    # Экранда шеңберді салу
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  # Экранда шеңбер салу

def drawRectangle(screen, start, end, width, color): 
    # Бастапқы және соңғы нүктелердің x және y координаттарын алу
    x1 = start[0]  # Бастапқы нүктенің x координатасын алу
    x2 = end[0]  # Соңғы нүктенің x координатасын алу
    y1 = start[1]  # Бастапқы нүктенің y координатасын алу
    y2 = end[1]  # Соңғы нүктенің y координатасын алу
    
    # Тікбұрыштың ені мен биіктігін есептеу
    widthr = abs(x1 - x2)  # Тікбұрыштың енін есептеу
    height = abs(y1 - y2)  # Тікбұрыштың биіктігін есептеу
    
    # Тікбұрышты экранда салу, бастапқы және соңғы нүктелердің орнына байланысты
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  # Экранда тікбұрыш салу
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  # Экранда тікбұрыш салу
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  # Экранда тікбұрыш салу
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)  # Экранда тікбұрыш салу

def drawSquare(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
    
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn)) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn)) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn)) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn)) 

def drawRightTriangle(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    
    if x2 > x1 and y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 

def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 

    width_b = abs(x2 - x1) 
    height = (3**0.5) * width_b / 2 

    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 

def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()  # Бағдарламаны терезе жабылғанда тоқтатады
         
        # Пернетақта оқиғаларын өңдеу
        if event.type == pygame.KEYDOWN: 
            # Нүкте бойынша режимді ауыстыру
            if event.key == pygame.K_r: 
                mode = 'rectangle'  # Тікбұрыш салу режиміне өту
            if event.key == pygame.K_c: 
                mode = 'circle'  # Шеңбер салу режиміне өту
            if event.key == pygame.K_p: 
                mode = 'pen'  # Қалам режиміне өту
            if event.key == pygame.K_e: 
                mode = 'erase'  # Өшіру режиміне өту
            if event.key == pygame.K_s: 
                mode = 'square'  # Квадрат салу режиміне өту
            if event.key == pygame.K_q: 
                screen.fill(pygame.Color('white'))  # Экранды ақ түспен тазалау

            # Пернені басу арқылы түсті өзгерту
            if event.key == pygame.K_1: 
                color = 'black'  # Түсті қараға өзгерту
            if event.key == pygame.K_2: 
                color = 'green'  # Түсті жасылға өзгерту
            if event.key == pygame.K_3: 
                color = 'red'  # Түсті қызылға өзгерту
            if event.key == pygame.K_4: 
                color = 'blue'  # Түсті көкке өзгерту
            if event.key == pygame.K_5: 
                color = 'yellow'  # Түсті сарыға өзгерту
            if event.key == pygame.K_t: 
                mode = 'right_tri'  # Оң жақ үшбұрыш салу режиміне өту
            if event.key == pygame.K_u: 
                mode = 'eq_tri'  # Тең бүйірлі үшбұрыш салу режиміне өту
            if event.key == pygame.K_h: 
                mode = 'rhombus'  # Ромб салу режиміне өту

        if event.type == pygame.MOUSEBUTTONDOWN:  
            draw = True  # Сурет салу режимін қосу
            if mode == 'pen': 
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)  # Қалам режимі қосылғанда шеңбер (пиксель) салу
            prevPos = event.pos  # Қазіргі орынды өткен орын ретінде сақтау

        if event.type == pygame.MOUSEBUTTONUP:  
            # Тінтуірдің батырмасы босатылғанда
            if mode == 'rectangle': 
                drawRectangle(screen, prevPos, event.pos, radius, color)  # Тікбұрыш салу
            elif mode == 'circle': 
                drawCircle(screen, prevPos, event.pos, radius, color)  # Шеңбер салу
            elif mode == 'square': 
                drawSquare(screen, prevPos, event.pos, color)  # Квадрат салу
            elif mode == 'right_tri': 
                drawRightTriangle(screen, prevPos, event.pos, color)  # Оң жақ үшбұрыш салу
            elif mode == 'eq_tri': 
                drawEquilateralTriangle(screen, prevPos, event.pos, radius, color)  # Тең бүйірлі үшбұрыш салу
            elif mode == 'rhombus': 
                drawRhombus(screen, prevPos, event.pos, radius, color)  # Ромб салу
            draw = False  # Сурет салуды тоқтату

        if event.type == pygame.MOUSEMOTION:  
            # Тінтуір қозғалғанда
            if draw and mode == 'pen': 
                drawLine(screen, lastPos, event.pos, radius, color)  # Қалам режимінде соңғы орын мен қазіргі орын арасындағы сызықты салу
            elif draw and mode == 'erase': 
                drawLine(screen, lastPos, event.pos, radius, 'white')  # Өшіру режимінде ақ сызықты салу
            lastPos = event.pos  # Соңғы орынды қазіргі орынмен жаңарту

    # Радиус туралы ақпаратты көрсету үшін тікбұрыш салу
    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))  # Радиус туралы ақпаратты көрсету үшін ақ тікбұрыш салу
    renderRadius = font.render(str(radius), True, pygame.Color(color))  # Ағымдағы радиус көрсетілген мәтінді жасау
    screen.blit(renderRadius, (5, 5))  # Мәтінді экранда көрсетілген орынға қою

    pygame.display.flip()  # Экранды жаңарту
    clock.tick(FPS)  # Кадр жылдамдығын басқару
