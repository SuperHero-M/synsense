import os
import shutil



def rm(path):
    rm_file = ['drinking(eating,calling).bin', 'inattentive.bin']
    for r, d, f in os.walk(path):
        if 'p01' in d and 'l01' in d:
            for i in d:
                dirs = os.path.join(r, i)
                if 'l' in i:
                    shutil.rmtree(dirs)
        if 'l03' in r:
            shutil.rmtree(r)
        for i in rm_file:
            if i in f:
                os.remove(os.path.join(r, i))


def cp(path):
    for r, d, f in os.walk(path):
        dir1 = r.replace('l0', 'k0')
        dir2 = dir1.replace('p0', 'l0')
        dir3 = dir2.replace('k0', 'p0')
        if not os.path.exists(dir3):
            os.makedirs(dir3)
        # for i in f:
        if len(f) != 0:
            for i in f:
                origin = (os.path.join(r, i))
                shutil.copyfile(origin, os.path.join(dir3, i))



cp('/home/maqitian/Downloads/20211223')
rm('/home/maqitian/Downloads/20211223')
