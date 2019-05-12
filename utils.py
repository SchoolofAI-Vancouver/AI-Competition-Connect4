import numpy as np

# output the index of when v has a continuous string of i
# get_runs([0,0,1,1,1,0,0],1) gives [2],[5],[3]
def get_runs(v, i):
    bounded = np.hstack(([0], (v==i).astype(int), [0]))
    difs = np.diff(bounded)
    starts, = np.where(difs > 0)
    ends, = np.where(difs < 0)
    return starts, ends, ends-starts

# see if vector contains N of certain number in a row
def in_a_row(v, N, i):
    if len(v) < N:
        return False
    else:
        _, _, total = get_runs(v, i)
        return np.any(total >= N) 
     
def get_lines(matrix, loc):

    i, j = loc
    flat = matrix.reshape(-1,*matrix.shape[2:])
    
    w = matrix.shape[0]
    h = matrix.shape[1]
    def flat_pos(pos):
        return pos[0]*h+pos[1]

    pos = flat_pos((i,j))

    # index for flipping matrix across different axis
    ic = w - 1 - i
    jc = h - 1 - j

    # top left
    tl = (i-j,0) if i>j else (0, j-i)
    tl = flat_pos(tl)

    # bottom left
    bl = (w-1-(ic-j),0) if ic>j else (w-1, j-ic)
    bl = flat_pos(bl)

    # top right
    tr = (i-jc,h-1) if i>jc else (0, h-1-(jc-i))
    tr = flat_pos(tr)

    # bottom right
    br = (w-1-(ic-jc),h-1) if ic>jc else (w-1, h-1-(jc-ic))
    br = flat_pos(br)

    hor = matrix[:,j]
    ver = matrix[i,:]
    diag_right = np.concatenate([flat[tl:pos:h+1],flat[pos:br+1:h+1]])
    diag_left = np.concatenate([flat[tr:pos:h-1],flat[pos:bl+1:h-1]])

    return hor, ver, diag_right, diag_left