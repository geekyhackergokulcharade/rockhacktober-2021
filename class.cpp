#include<iostream>
using namespace std;

class a {
    public:
    int a;
    void funca(){
        cout<<"funca"<<endl;
    }
    private:
    void funcb(){
        cout<<"funcb"<<endl;
    }
    protected:
    void funcc(){
        cout<<"funcc"<<endl;
    }

};
int main(){
    a obj;
    //obj.funca();
    obj.funcc();


}