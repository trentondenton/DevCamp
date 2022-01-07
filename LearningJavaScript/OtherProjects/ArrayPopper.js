class ArrayPopper {
    constructor(arr) {
        this.arr = arr;
        this.atBeginning = true;
    }
    togglePopper() {
        this.atBeginning = !this.atBeginning;
        return this.atBeginning ? this.arr.pop() : this.arr.shift();
    }  
}



