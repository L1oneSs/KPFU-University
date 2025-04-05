# -*- coding: utf-8 -*-
import secrets


def power_mod(b, e, m):
    """Быстрое возведение в степень по модулю"""
    res = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            res = (res * b) % m
        e = e // 2
        b = (b * b) % m
    return res


def find_s_d(p):
    """p − 1 = 2^s * d\n
    d - нечётное число, s - кол-во раз, которое 2 можно делить на p−1"""
    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    return s, d


def is_composite(a, d, s, n):
    """Проверяет, является ли число составным"""
    x = power_mod(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(s - 1):
        x = power_mod(x, 2, n)
        if x == n - 1:
            return False
    return True


def miller_rabin_test(p, n=None):
    if p in [1, 2, 3, 5, 7]:
        return True
    if n is None:
        n = int(p).bit_length() // 2

    s, d = find_s_d(p)
    for _ in range(n):
        a = secrets.randbelow(p - 2) + 2
        if is_composite(a, d, s, p):
            return False
    return True


def gcd(a, b):
    """Возвращает наибольший общий делитель a и b"""
    while b != 0:
        a, b = b, a % b
    return a
