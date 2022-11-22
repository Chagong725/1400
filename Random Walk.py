"docstring"
import subprocess
import tempfile
import random
import sys
import numpy
import turtle
import math

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs',
                        '-dSAFER',
                        '-o',
                        dest,
                        '-r200',
                        '-dEPSCrop',
                        '-sDEVICE=png16m',
                        tmp.name],
                       stdout=subprocess.DEVNULL)

def output(walker, steps, arr): #출력 함수
    "docstring"
    arr_mean = numpy.round(numpy.mean(arr), 1) #평균
    arr_max = numpy.round(max(arr), 1) #최대
    arr_min = numpy.round(min(arr), 1)  #최소
    arr_cv = numpy.round((numpy.std(arr) / arr_mean), 1) #분산

    #출력
    print(f'{walker} random walk of {steps} steps')
    print(f'Mean = {arr_mean:.1f} CV = {arr_cv:.1f}')
    print(f'Max = {arr_max:.1f} Min = {arr_min:.1f}')

def move(walk_lengths, number_trials, point, walker, tur): #각 캐릭터에 따라 좌표이동
    "docstring"
    plot_list = []
    for walk_len in walk_lengths: #걸음 수에 따라 테스트 진행
        distance = [] #마지막에 원점에서 부터 마지막 위치까지의 거리 저장
        for _ in range(number_trials): #테스트 횟수만큼 반복
            _x, _y = 0, 0 #초기 위치 (_x 이딴식으로 하면 스네이크안걸리던데?ㅋㅋㅋ)
            for _ in range(walk_len): #걸음수만큼 좌표 무작위로 이동
                _dx, _dy = random.choice(point) #이동 가능 경로중에서 하나 뽑기
                _x += _dx
                _y += _dy
            distance.append(((_x**2) + (_y**2))**(0.5)) #피타고라스 정리로 걍함
            if len(plot_list) < 50:
                plot_list.append([_x, _y])
        if tur:
            return plot_list
        else:
            output(walker, walk_len, distance) #모든 테트스 완료후에 출력으로 넘기기
    return 0

def simulate(walk_lengths, number_trials, walker):
    "doc"
    if walker == 'Pa':
        point = [(0,1), (1,0), (0,-1), (-1,0)]
        move(walk_lengths, number_trials, point, 'Pa', False)
    elif walker == 'Mi-Ma':
        point = [(0,1), (1,0), (0,-1), (0,-1), (-1,0)]
        move(walk_lengths, number_trials, point, 'Mi-Ma', False)
    elif walker == 'Reg':
        point = [(1,0), (-1,0)]
        move(walk_lengths, number_trials, point, 'Reg', False)
    else:
        point = [(0,1), (1,0), (0,-1), (-1,0)]
        move(walk_lengths, number_trials, point, 'Pa', False)
        point = [(0,1), (1,0), (0,-1),(0,-1), (-1,0)]
        move(walk_lengths, number_trials, point, 'Mi-Ma', False)
        point = [(1,0), (-1,0)]
        move(walk_lengths, number_trials, point, 'Reg', False)

def plot():
    """tu"""
    turtle.setup(width = 300, height = 400)
    t_walk = turtle.Turtle()
    t_walk.shapesize(0.5)
    t_walk.speed(0)
    t_walk.penup()
    t_walk.shape('circle')
    t_walk.color("black")
    plot_list = move([100], 50, [(0,1), (1,0), (0,-1), (-1,0)],'Pa', True)
    for t_x, t_y in plot_list:
        t_walk.goto(t_x*5, t_y*5)
        t_walk.stamp()
    plot_list = move([100], 50, [(0,1), (1,0), (0,-1),(0,-1), (-1,0)], 'Mi-Ma', True)
    t_walk.shape('square')
    t_walk.color('green')
    for t_x, t_y in plot_list:
        t_walk.goto(t_x*5, t_y*5)
        t_walk.stamp()
    plot_list = move([100], 50, [(1,0), (-1,0)], 'Reg', True)
    t_walk.shape('triangle')
    t_walk.color("red")
    for t_x, t_y in plot_list:
        t_walk.goto(t_x*5, t_y*5)
        t_walk.stamp()
    save_to_image('random_walk.png')

def main():
    "docstring"
    walk_lengths =  list(map(int, (sys.argv[1]).split(',')))
    number_trials = int(sys.argv[2])
    walker = sys.argv[3]
    plot()
    simulate(walk_lengths, number_trials, walker)

if __name__ == "__main__":
    main()
