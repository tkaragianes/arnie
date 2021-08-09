from arnie.utils import *

bp_list = [[1, 53], [2, 52], [3, 51], [4, 50]]
bpseq_file = "test_files/seq.bpseq"
ct_file = "test_files/seq.ct"
prob = [[0.000000000000000000e+00, 0.000000000000000000e+00, 1.763635280966738210e-08, 3.609733185304499478e-10, 1.899559890269620151e-08, 2.357239330957941875e-08, 4.468964148624955998e-08, 1.829342375496644303e-07, 4.127057055650768230e-06, 6.457873937490533129e-06, 5.384244594784908830e-06, 2.036780995975695890e-06, 8.030412357417303880e-05, 9.388004334808641715e-01],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 7.471370797708187664e-11, 1.984224746020934790e-09, 1.454165406835343696e-07, 7.498508237767878982e-07, 3.865106868873978322e-06, 3.536102881585034987e-05, 2.394675941956625451e-05, 1.153705070502445834e-05, 2.612278010790368161e-04, 9.977645040109642816e-01, 3.237492435080424613e-02],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.888956084283119840e-07, 5.413485565351087927e-07, 1.541276902667509429e-06, 1.126288121100931219e-05, 1.173869736654523994e-04, 7.325411664786217837e-06, 4.003005106708449522e-05, 9.983489958892994842e-01, 6.129986080705812287e-03, 1.054258712935700630e-04],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.665249372829090312e-07, 9.497187209883291010e-06, 1.414039620915108573e-04, 3.243636730206535555e-05, 1.567102777497324565e-05, 9.975833150208464062e-01, 5.034934175522413902e-03, 4.125712961733680345e-04, 2.274785721191600433e-07],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.738593674907211730e-05, 8.545859784264292502e-05, 3.527927141337322309e-04, 9.980848491909390940e-01, 5.202587741165264415e-03, 1.251151206947209791e-04, 8.513900403421354130e-05, 2.669391452879514996e-07],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 4.533978023581152796e-03, 6.727278019311770663e-02, 6.385230293170572440e-04, 1.043096878283355517e-05, 5.352860417885025332e-05, 2.197980140741698389e-06, 7.290393039203351602e-07],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 2.247207617456368913e-06, 1.250804117783563030e-06, 1.540204172157810605e-05, 6.227562675838443224e-05, 4.136123245159868602e-06, 1.480250050762932428e-06],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 5.317539514120537016e-08, 1.466432823612201115e-06, 4.843728467860043972e-05, 9.024276054982824927e-06, 5.084605728081093467e-07],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.142360160134971489e-07, 2.745012688262551338e-05, 2.086567406564575274e-05, 2.143480176383162954e-06],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.219164078076087741e-06, 1.118464018225010500e-05, 7.100719490463872321e-06],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 4.536954583383731369e-06, 9.361786362639244079e-06],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 1.650802739207468036e-06],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00],
        [0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00, 0.000000000000000000e+00]]
prob_file = "test_files/seq.prob"


def test_file_converters():
    assert(bpseq_to_bp_list(bpseq_file, header_length=1) == bp_list)
    assert(ct_to_bp_list(ct_file, header_length=2) == bp_list)
    assert(prob_to_bpp(prob_file).tolist() == prob)
    assert(bpseq_to_bp_list(bpseq_file, header_length=3) != bp_list)
    assert(ct_to_bp_list(ct_file, header_length=4) != bp_list)

if __name__ == '__main__':
    test_file_converters()
