
#include<iostream>
using namespace std;

int sum(int n){
	if(n==0) return 0;
	int sumi = 0;
	for(int i; i<=n; i++){
		sumi+= i;
	}
	return sumi;
}
int main(){
	int p= 50;
	cout<<sum(p)<<endl;
}
