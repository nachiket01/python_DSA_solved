#include <bits/stdc++.h>
using namespace std;

int main()
{

	int a,b,i,j, flag;

	count<<"Enter lower bound of interval: ";
	cin>> a;
	count<<"Enter upper bound of interval: ";
	cin>> b;	

	cout<<"\n Prime numbers between"<<a<<"and"<<b<<"are : ";
	for(i=a; i<=b; i++){

		if(i == a || i == 0)
			continue;

		flag =1;

	for(j=2;j<=1/2;++j){

		if(i % j == 0){
			flag = 0;
			break
		}
	}
	if(flag == 1)
		cout<<i<<" ";

	}
	return 0;
}