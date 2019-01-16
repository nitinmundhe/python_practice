msg = 'Module Demo'


def sub(a, b):
    return 'Sub of {} and {} is {} '.format(a, b, a - b)

if __name__ == '__main__':
    print('Message = ',msg)
    print('Sub = ',sub(50, 20))
    print('name',__name__)