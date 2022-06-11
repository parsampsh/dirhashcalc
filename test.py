import dirhashcalc

assert dirhashcalc.DirHashCalculator('test-dir').calc() == 'ec6184e3cf4fe9b033faa8c54d06a7cb4f0acfc9dd7201c07af7f64cf6cd5350'

print('PASS')
