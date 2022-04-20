#include <iostream>
using namespace std;

class FullList{};
class EmptyList{};

template <class ItemType>
struct NodeType{
    ItemType info;
    NodeType* next;

    NodeType(){
        info = NULL;
        next = NULL;
    }
};

template <class ItemType>
class UnsortedLL{
private:
    int length;
    NodeType<ItemType>* head;

public:
    UnsortedLL(){
        length = 0;
        head = new NodeType<ItemType>;
    }

    bool isFull(){
        try{
            NodeType<ItemType>* temp = new NodeType<ItemType>;
            delete temp;
            return false;
        }
        catch(const bad_alloc& e){
            return true;
        }
    }

    int isLength(){
        return length;
    }

    bool isEmpty(){
        return (length == 0);
    }

    void insertItem(ItemType item){
        if(isFull())
            throw FullList();

        NodeType<ItemType>* newItem = new NodeType<ItemType>;
        NodeType<ItemType>* location = head;
        newItem -> info = item;
        newItem -> next = NULL;

        while(location -> next != NULL)
            location = location -> next;
        location -> next = newItem;

        length++;
    }

    void deleteItem(ItemType item){
        if (isEmpty())
            throw EmptyList();

        NodeType<ItemType>* location = head -> next;
        NodeType<ItemType>* prevLoc = head;

        bool moreToSearch = true;
        while(moreToSearch) {
            if(location -> info == item){
                prevLoc -> next = location -> next;
                length--;
                delete location;
                moreToSearch = false;
            }
            else{
                prevLoc = location;
                location = location -> next;
                moreToSearch = (location != NULL);
            }
        }
    }

    int retrieveItem(ItemType item){
        NodeType<ItemType>* location = head -> next;

        bool moreToSearch = true;
        bool found = false;
        int count = 0;
        while(moreToSearch and !found) {
            if (location->info == item){
                found = true;
                return count;
            }
            else{
                location = location -> next;
                count++;
                moreToSearch = (location != NULL);
            }
        }
        return -1;
    }

    ItemType at(int index){
        NodeType<ItemType>* location = head -> next;
        for(int i = 0; i < index; i++){
            location = location -> next;
        }

        return location->info;
    }

    void print(){
        NodeType<ItemType>* location = head -> next;
        cout << '[';
        while(location != NULL) {
            if(location -> next != NULL)
                cout << location -> info << ", ";
            else
                cout << location -> info;
            location = location->next;
        }
        cout << ']' << endl;
    }
};

