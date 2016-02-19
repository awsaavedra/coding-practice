function find_deviation(v, d) {
    var seq = [];
    var median = 0;
    for(var k = 0; k < d; k++) {
        seq.push(v[k]);
    }

    var localMedian = find_median(seq);
    if(localMedian > median) {
        median = localMedian;
    }

    for(var i = d; i < v.length; i++) {
        seq.shift();
        seq.push(v[i]);
        var locMedian = find_median(seq);
        if(locMedian > median) {
            median = locMedian;
        }
    }

    return median;
}

function find_median(seq) {
    var localMin = Math.min.apply(Math, seq);
    var localMax = Math.max.apply(Math, seq);
    return localMax - localMin;
}
console.log(find_deviation([6,9,4,7,1], 3));
