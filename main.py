# coding=utf-8
import scipy.special as scsp


def million_gacha(ssr_number, all_number, ssr_p):
    pattern = scsp.comb(all_number, ssr_number, True)
    all_ssr_p = ssr_p**ssr_number
    all_non_ssr_p = (1-ssr_p)**(all_number-ssr_number)

    return pattern*all_ssr_p*all_non_ssr_p


def million_fes(ssr_number):
    return million_gacha(ssr_number, 50, 0.06)


def normal_gatya(ssr_number):
    return million_gacha(ssr_number, 90, 0.03)


def ssr_probability(ssr_number):
    probability = 0
    for i in range(ssr_number+1):
        probability += million_fes(i)*normal_gatya(ssr_number-i)
    return probability


if __name__ == '__main__':
    N = 30
    sum_probability = 0
    for i in range(N):
        sum_probability += ssr_probability(i)
        if ssr_probability(i) < 0.1:
            if sum_probability < 0.1:
                print("SSRが{0:3d}枚出る確率:  {1:10.8%},  {2:10.8%}".format(i, ssr_probability(i), sum_probability))
            else:
                print("SSRが{0:3d}枚出る確率:  {1:10.8%}, {2:10.8%}".format(i, ssr_probability(i), sum_probability))
        else:
            print("SSRが{0:3d}枚出る確率: {1:10.8%}, {2:10.8%}".format(i, ssr_probability(i), sum_probability))
