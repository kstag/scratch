#!/usr/bin/env python
from itertools import permutations

versions = ['old', 'new']

order = []
for i in permutations(['car', 'cmc', 'sdrs']):
    order.append(i)

fw = {}
fw['old'] = {'car': '/ifs/car_fw_old.hpm',
             'cmc': '/ifs/cmc_fw_old.hpm',
             'sdrs': '/ifs/sdrs_old.bin'}
fw['new'] = {'car': '/ifs/car_fw_new.hpm',
             'cmc': '/ifs/cmc_fw_new.hpm',
             'sdrs': '/ifs/sdrs_new.bin'}

for cur_ver in versions:
    perm = 0
    print('========== Version {0} =========='.format(cur_ver))
    for cur_order in order:
        perm += 1
        print('\nPermutation {0} - == Current device ordering {1} =='
              .format(perm, cur_order))
        print('-'*80)
        for dev in cur_order:
            print('Device {0} has {1} fw at {2}'.format(dev, cur_ver, fw[cur_ver][dev]))
