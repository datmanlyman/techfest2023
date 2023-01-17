const totalJobClass = 5;
let quizResults = [];
let ranking = [];

for (let i = 0; i < totalJobClass; i++) {
    quizResults.push(0);
}

function getAnswer() {
    var radioID = document.querySelector('input[name="inlineRadioOptions"]:checked').id;
    var result = radioID.substring(radioID.length - 1);
    quizResults[parseInt(result) - 1] += 1;
    console.log(quizResults);
}

function heapSort() {
    let heap = quizResults;
    let map = createMap(heap);
    console.log(map)
    buildMaxHeap(heap);

    for (let endIdx = heap.length - 1; endIdx > 0; endIdx--) {
        swap(0, endIdx, heap);
        siftDown(0, endIdx - 1, heap);
    }

    endIdx = heap.length - 1;
    startIdx = 0;
    while (startIdx < endIdx) {
        swap(startIdx, endIdx, heap);
        startIdx += 1;
        endIdx -= 1;
    }

    for (let idx = 0; idx < totalJobClass; idx++) {
        const jobClass = map.get(heap[idx]).pop();
        ranking.push(jobClass);
    }

    localStorage.setItem("ranking", ranking);
    localStorage.setItem("heap", heap);
    window.location.href = 'result';
}

function createMap(array) {
    let map = new Map();
    for (let idx = 0; idx < totalJobClass; idx++) {
        if (!(map.has(array[idx]))) {
            map.set(array[idx], [referTable(idx)]);
        } else {
            map.set(array[idx], [...map.get(array[idx]), referTable(idx)]);
        }
    }
    return map;
}

function referTable(idx) {
    switch (idx) {
        case 0:
            return "Software Engineering";
        case 1:
            return "Cyber Security";
        case 2:
            return "Hardware";
        case 3:
            return "AI";
        case 4:
            return "System Analyst";
    }
}

function buildMaxHeap(heap) {
    const firstParentIdx = Math.floor((heap.length - 2) / 2);
    for (let currentIdx = firstParentIdx; currentIdx >= 0; currentIdx--) {
        siftDown(currentIdx, heap.length - 1, heap);
    }
}

function siftDown(currentIdx, endIdx, heap) {
    let childOneIdx = (currentIdx * 2) + 1;
    while (childOneIdx <= endIdx) {
        // If (currentIdx * 2) + 2 <= endIdx, then childTwoIdx = (currentIdx * 2) + 2, else -1
        const childTwoIdx = (currentIdx * 2) + 2 <= endIdx ? (currentIdx * 2) + 2 : -1;
        let idxToSwap = (childTwoIdx !== -1 && (heap[childTwoIdx] > heap[childOneIdx])) ? childTwoIdx : childOneIdx;
        if (heap[idxToSwap] > heap[currentIdx]) {
            swap(currentIdx, idxToSwap, heap);
            currentIdx = idxToSwap;
            childOneIdx = (currentIdx * 2) + 1;
        } else {
            return;
        }
    }
}

function swap(i, j, array) {
    const temp = array[j];
    array[j] = array[i];
    array[i] = temp;
}
