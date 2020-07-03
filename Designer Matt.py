
if __name__ == '__main__':
    c = '.|.'
    n, m = map(int, input().split())
    pattern = [(c*(2*i+1)).center(m, '-') for i in range(n//2)]
    print('\n'.join(pattern + ['Welcome'.center(m,'-')] + pattern[::-1]))


#print('\n'.join(pattern))
#print('\n'.join(pattern)[::-1])

#print((c*1).center(21,'-'))
#print((c*3).center(21,'-'))
#print((c*5).center(21,'-'))
#print("Welcome".center(21,'-'))
#print((c*5).center(21,'-'))
#print((c*3).center(21,'-'))
#print((c*1).center(21,'-'))