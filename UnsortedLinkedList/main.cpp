#include <iostream>
#include "Unsorted.h"

int main() {
    UnsortedLL<int> arr;

    arr.insertItem(4);
    arr.insertItem(3);
    arr.insertItem(5);
    arr.insertItem(1);
    arr.insertItem(2);

    for(int i = 0; i < arr.isLength(); i++){
        cout << i+1 << "번째 요소: " << arr.at(i) << endl;
    }

    cout << "리스트 길이: " << arr.isLength() << endl;
    cout << "리스트: ";
    arr.print();


    arr.deleteItem(3);
    arr.deleteItem(2);
    arr.deleteItem(2);
    arr.deleteItem(1);


    for(int i = 0; i < arr.isLength(); i++){
        cout << i+1 << "번째 요소: " << arr.at(i) << endl;
    }

    cout << "리스트 길이: " << arr.isLength() << endl;
    cout << "리스트: ";
    arr.print();

}
