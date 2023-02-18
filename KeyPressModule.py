import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


# function to get key presses
def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass  # check events
    keyInput = pygame.key.get_pressed()  # create inputs, specific format
    myKey = getattr(pygame, 'K_{}'.format(keyName))  # specific format for K_{}
    # K_{LEFT}
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")
    # print(getKey("a"))


if __name__ == '__main__':
    init()
    while True:
        main()
