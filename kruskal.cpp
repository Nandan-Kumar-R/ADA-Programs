#include <iostream>
using namespace std;
int w[10][10],no[45],edge[45],par[10];

int parent(int i)
{int j=i;
  while(par[j]!=j)
   j=par[j];
   return j;
}

int main()
{int n,i,j,temp,u,v,p=0,k=0;
cout<<"enter the number of vertices"<<endl;
cin>>n;
cout<<"enter the weighted matrix"<<endl;
for(i=0;i<n;i++)
{
    for(j=0;j<n;j++)
    cin>>w[i][j];
}
for(i=0;i<n;i++)
    par[i]=i;
for(i=0;i<n-1;i++)
{
    for(j=i+1;j<n;j++)
    {no[p]=w[i][j];
     edge[p]=(i*10)+j;
     p++;

    }
}
for(i=0;i<p-1;i++)
{
    for(j=i+1;j<p;j++)
    {
        if(no[j]<no[i])
        {
            temp=no[i];no[i]=no[j];no[j]=temp;
            temp=edge[i];edge[i]=edge[j];edge[j]=temp;
        }
    }
}
i=0;
cout<<"\nMinimum spanning tree is\n";
while(k<n-1)
{u=parent(edge[i]/10);
 v=parent(edge[i]%10);
 if(u!=v)
 {cout<<edge[i]/10<<"->"<<edge[i]%10<<"----"<<w[edge[i]/10][edge[i]%10]<<endl;
  k++;
  par[v]=u;
 }
    i++;
}
return 0;
}



