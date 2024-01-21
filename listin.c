# include <stdio.h>
void main(){
   int x=1,y=2,z=3,n=4;

    for(int i=0;i<=x;i++){
        for(int j=0;j<=y;j++){
            for(int k=0;k<=z;k++){
                if((i+j+k)!=n){
                    printf("%d %d %d\n",i,j,k);
                }
            }
        }
    }
}