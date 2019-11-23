from costs import cost
from costs import sale
import time

while True:
    # examples you can add more or delete if you like to do so!
    # usage sale(cost('URL', price, gametitle))
    sale(cost('https://www.cdkeys.com/pc/games/prey-pc'), 3.99, 'Pray')
    sale(cost('https://www.cdkeys.com/pc/games/middle-earth-shadow-of-mordor-game-of-the-year-edition-pc-cd-key'), 2.99, 'Shadow of Mordor')
    sale(cost('https://www.cdkeys.com/pc/games/dying-light-pc-cd-key-steam'), 6.99, 'Dying Light')
    sale(cost('https://www.cdkeys.com/pc/games/assassins-creed-odyssey-pc-uplay-cd-key'), 19.99, 'Odyssey')
    sale(cost('https://www.cdkeys.com/pc/games/the-hunter-call-of-the-wild-pc-steam-cd-key'), 14.99, 'The Hunter')
    sale(cost('https://www.cdkeys.com/pc/games/call-of-duty-4-modern-warfare-pc-cd-key-steam'), 6.99, 'COD:MW')

    # time interval in seconds calculated to days!
    time.sleep(3600 * 24)