#include<stdio.h>
#include<conio.h>
#include<dos.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
/*
200 left down
201 left top
187 top right
188 bottom right
186 col
205 row
206 plusdoubleline
*/
/*
ng-random or whatever,gridboard,setboard,play in while till complete or saved
lg-loads board from saved enrypted cfile
*/
void delprnt(char *s,int d,int x, int y);
void borderline(int x,int y,int x1,int y1);
void shuffle(int arr[81]);
void play(char *brel,char *trel,int x,int y);
//print grid
void printGrid(char grid[81]){
	int i;
	for(i = 0; i < 81; i++){
		if(i %9==0)
			printf("\n");
		printf("%c ",grid[i]);
	}
}

//read cs
void read(char *data){
	strcpy(data,"123456789789123456456789123512647938934815267867932514248371695395264871671598342");
	/*FILE *fp = fopen("abc.txt","r");
	//if(fp==NULL)
	//	printf("Error\n");
	//for(i = 0; i < 10; i++){
	//	c=0;
while((ch=fgetc(fp)) != '\n'){
			data[i][c] = ch;
			c++;
		}
	}

	for(int i = 0 ; i< 10; i++){

		for(int j = 0; j < 81; j++){

			printf("%c ",data[i][j]);

		}printf("\n");
	}
	fclose(fp);
	*/
}

//read random grid
void getGrid(char data[10][81], int ln, char grid[81]){
/*
	strcpy(grids[0],strtok(data,"\n"));
	printf("%s\n",grids[0]);
	for(int i = 1; i < 10;i++){
		strcpy(grids[i],strtok(NULL,"\n"));
		printf("%s\n",grids[i]);
	}*/
	int i;
	int max = 810 - 81*(9-ln);
	//int n = 0;
	for(i = 0;i < 81;i++){
		grid[i] = data[ln][i];
		//n++
	}
}

//function to choose random grid
void pickGrid(int *n){
	srand(time(NULL));
	*n = (rand()%10);
}

//function to randomly pop elements of the grid
void makePuzzle(char puzzle[81]){
	int arr[81],i;
	shuffle(arr);
	for(i = 0; i < 33; i++){
		int pos = arr[i];
		puzzle[pos] = ' ';
	}
}

//fisher yates algorithm

void shuffle(int arr[81]){
	int i,j,temp;
	for(i = 0; i < 81; i++)
		arr[i] = i;
	// Use a different seed value so that we don't get same
	srand ( time(NULL) );
	// Start from the last element and swap one by one. We don't
	// need to run for the first element that's why i > 0
	for (i = 80; i > 0; i--) {
	// Pick a random index from 0 to i
		j = rand() % (i+1);
	// Swap arr[i] with the element at random index
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
    }

}

void congratulate()
{
	borderline(80,24,30,10);
	delprnt("CONGRATULATIONS!!!\n\n",50,30,10);
	delprnt("You have beat the board!",50,30,15);
	delay(2000);
}

void saveas(char *brel,char *trel)
{
	borderline(80,24,30,10);
	delprnt("Coming soon...",30,30,10);delay(2000);
	//same as save, but stores differently.
}

void save(char *brel,char *trel)
{
	borderline(80,24,30,10);
	delprnt("Coming soon...",30,30,10);delay(2000);
	//inputs the name of the file and stores it in directory same as source file
	//if file is saved before, overwrite
}

void timeit()
{
	borderline(80,24,30,10);
	delprnt("Coming soon...",30,30,10);delay(2000);
	//will time the total duration the play code runs for
}

int arraycmp(char *a1,char *a2)
{
	//compares 2 arrays, here soln and user input.
	int i;
	for(i=0;i<81;i++)
	{
		if(!(*(a1+i)==*(a2+i)))
			return 0;
	}
	return 1;
}
void igmenu()
{
	//in game menu, accessed by an input.
	borderline(80,24,30,10);
	delprnt("In Game menu will be released soon.",100,30,10);
	delay(2000);

}
void randomboard(int x,int y)
{
	//A random function must come here
	char data[81],grid[81],puzzle[81];int ln;
	read(data);
	//pickGrid(&ln);
	//getGrid(data,ln,grid);
	strcpy(puzzle,data);
	makePuzzle(puzzle);
	play(puzzle,data,x,y);
}
void randombiboard()
{
	//Built in boards, so file handlers
}
void play(char *brel,char *trel,int x,int y)
{
	int ex=1,i,j=0,blanks[81],bno=0,bx=0,by=0;
	char c;
	//fnction to go through the board via WASD or AD
	//goes through,gets the values (if non number, dont do anything
	//if number (valid), update brel and setboarding
	while(ex)
	{
		for(i=0;i<81;i++)
		{
		    if(brel[i]==' ')
			{blanks[j]=i;j++;}
		}
		setboard(brel,blanks,bno,x,y,&bx,&by);
		gotoxy(bx,by);
		c=getch();
		switch(c)
		{
		case 'a':
		case 'A':{bno--; break;}
		case 'd':
		case 'D':{bno++;break;}
		case 'm':
		case 'M':{igmenu();break;}
		case '1':
		case '2':
		case '3':
		case '4':
		case '5':
		case '6':
		case '7':
		case '8':
		case '9':{brel[blanks[bno]]=c;break;}
		case 'E':
		case 'e':{ex=0;break;}
		default:{;}
		}
		if(arraycmp(brel,trel)==1)
		{
			congratulate();
			break;
		}
	}
}
void settings(int x,int y)
{
	borderline(80,24,x,y);
	delprnt("Nothing to control, yet!",50,x,y);
	delay(2000);
}
void borderline(int x,int y,int x1,int y1)
{
	int i,j,k;
	clrscr();
	for(i=1;i<=y;i++)
	{
		if(i==1||i==y)
		{
			gotoxy(1,i);
			k=(i==1)?201:200;
			printf("%c",k);
			for(j=2;j<x;j++)
				printf("%c",205);
			k=(i==1)?187:188;
			printf("%c",k);
		}
		else
		{
			gotoxy(1,i);
			printf("%c",186);
			gotoxy(x,i);
			printf("%c",186);
		}
	}
	gotoxy(x1,y1);
}
void credits(int x,int y)
{
	borderline(80,24,x,y);
	delprnt("CREDITS:\n\n\0",100,x,y);
	delprnt("Shubham Gupta - Logical guy\n\0",20,5,wherey());delay(2000);
	delprnt("Random function algorithm,sudoku generator algorithm,File Handling.\n\0",20,5,wherey());delay(500);
	delprnt("Vishnu Gopakumar - Sudoku board data, management,File Handling.\n\0",20,5,wherey());delay(500);
	delprnt("Gaurika Poplai - Research and resources, File Handling.\n\0",20,5,wherey());delay(500);
	delprnt("Mohit Sharma - Front End, Graphics, FX, File Handling.\n\n\n\0",20,5,wherey());delay(500);
	delprnt("Thanks to all others who helped contribute in some way or the other.\n\0",20,5,wherey());
	getch();
	getch();
}
int setstart(int *xst,int *yst)
{
	int i;
	*xst=0;
	for(i=0;;i++)
	{
		if(wherey()>1)
			break;
		printf(" ");
		(*xst)++;
	}
	*xst-=13;
	*xst/=2;
	*yst=6;
	return 0;
}
void gridboard(int x,int y)
{
	int i,j;
	gotoxy(x-1,y-1);
	for(i=1;i<=13;i++)
	{
		if(i==1||i==13)
		{
			for(j=1;j<=25;j++)
				if(j!=1||j!=25)
					printf("%c",205);
				else if(j==1)
				{
					if(i==1) printf("%c",201);
					else printf("%c",187);
				}
				else
				{
					if(i==1) printf("%c",200);
					else printf("%c",188);
				}

		}
		else
		{
			gotoxy(x-1,i);
			printf("%c",186);
			gotoxy(x+23,i);
			printf("%c",186);
		}
	}
}
int setboard(char brel[81],char blanks[81],int bno,int xst,int yst,int*xp,int*yp)
{
	int once=0,bracket=0;
	int i,j,m=0,xpp,ypp;
	char cc;
	int xblanks[81],yblanks[81];
	int k=0,l=0;
	int loc=blanks[bno];
	borderline(80,24,xst,yst);
	//gridboard(xst,yst);
	//textcolor(RED);
	//textbackground(WHITE);
	//printf("\n\n");
	//gotoxy(xst,yst);
	for(i=0;i<=8;i++)
	{
		//	printf("                                                ");//48spaces for normal view of 120 as 23 chars in grid horiz
		gotoxy(xst,wherey());
		printf("");
		if(once||(i!=3&&i!=6))
		{
			once=0;
			for(j=0;j<=8;j++)
			{
				cc=brel[(9*i)+j];
				if(j==0)
					printf(" ");
				if(j==3||j==6)
				{
					printf("%c %1c ",186,cc);
					if(((9*i)+j)==blanks[m])
					{
					m++;
					xpp=wherex();
					ypp=wherey();
					gotoxy((xpp)-3,(ypp));
					printf("[");
					gotoxy((xpp)-1,(ypp));
					printf("]");
					gotoxy(xpp,ypp);
					bracket=1;
					}
				}
				else
				{
					printf("%1c",cc);
					printf(" ");
					if(((9*i)+j)==blanks[m])
					{
					m++;
					xpp=wherex();
					ypp=wherey();
					gotoxy((xpp)-3,(ypp));
					printf("[");
					gotoxy((xpp)-1,(ypp));
					printf("]");
					gotoxy(xpp,ypp);
					}
				}
				if(((9*i)-j)==loc)
				{
					*xp=wherex();
					*yp=wherey();
				}
			}
		}
		else
		{
			once=1;
			i--;
			for(j=0;j<=8;j++)
			{
				if(j==0)
					printf("%c%c%c",205,205,205);
				else if(j==3||j==6)
					printf("%c%c%c%c",206,205,205,205);
				else
					printf("%c%c",205,205);
			}
		}
	       //	printf("                                                 ");//49sp acting as lineenders
		printf("\n");
	}
	gotoxy(xst,yst);
	getch();
       //	printf("                                                0 0 0");
	return 0;
}
void newgame(int x,int y)
{
       char ch;
       //int i,j;char c[81],a='0';
       //for(i=0;i<=8;i++,a='0')
       //for(j=0;j<=8;j++,a++)
       //c[(i*9)+j]=a;
       //setboard(c,x,y);
       //getch();
       borderline(80,24,1,1);
       /*delprnt("What should be done?\n\n\0",50,x,y);
       gotoxy(x,wherey());
       delprnt("1. Random Board (needs time to generate)\n\0",50,x-8,wherey());
       gotoxy(x,wherey());
       delprnt("2. Built-in Board(predefined)\n\0",50,x-8,wherey());
       ch=getch();
       switch(ch)
       {
		case '1':
		case 'R':
		case 'r':{randomboard();break;}
		case '2':
		case 'B':
		case 'b':
		case 'P':
		case 'p':{randombiboard();break;}
       }*/
       delprnt("LOADING BOARD...",200,x-2,y);
       randomboard(x,y);
}
void loadgame(int x,int y)
{
	delprnt("Coming soon...",200,x-2,y);
	delay(2000);
	//displays available save games, asks to input your savefile.
}
void delprnt(char *s,int d,int x,int y)
{
	gotoxy(x,y);
	while(*s!='\0')
	{
		printf("%c",*s);
		s++;
		delay(d);
	}
}
int main()
{	int x,y,ext=0;
	int first=1;
	char brel[81],ch='`';
	borderline(80,24,1,1);
	while(ext==0)
	{
		if(first==1)
		{
			setstart(&x,&y);
			delprnt("...............",200,x,y);
			textcolor(YELLOW);
			textbackground(RED);
			delay(2000);
			clrscr();
			borderline(80,24,x,y);
		}
		if(first==1)
		{
			textcolor(YELLOW);
			delprnt("S U P R E M E\0",200,x,y+5);
			printf("\n");
			delprnt(" S U D O K U\0",200,x,wherey());
			textcolor(YELLOW);
			delay(1200);
			gotoxy(x,wherey()+3);
			delprnt("An application by Team GMSV!\0",100,x-7,wherey());
			delay(3000);
			delline();
			gotoxy(x,wherey());
			delprnt("PRESS TO START",50,x,wherey());
			gotoxy(1,1);
			getch();
			first=0;
		}
		else
		{
			borderline(80,24,x,y);
			textcolor(YELLOW);
			textbackground(RED);
			printf("S U P R E M E \n");
			gotoxy(x,wherey());
			printf(" S U D O K U");
		printf("\n\n\n\n");
		gotoxy(x,wherey());
		printf("1. NEW GAME\n\n");
		gotoxy(x,wherey());
		printf("2. LOAD GAME\n\n");
		gotoxy(x,wherey());
		printf("3. EXIT GAME\n\n");
		ch=getch();
		switch(ch)
		{
			case 'N':
			case 'n':
			case '1':{newgame(x,y);break;}
			case 'L':
			case 'l':
			case '2':{loadgame(x,y);break;}
			case 'Q':
			case 'q':
			case 'E':
			case 'e':
			case '3':{clrscr();borderline(80,24,x,y);printf("Are you sure? (Y/N)");
				ch=getch();
				if(ch=='Y'||ch=='y') {clrscr();
				gotoxy(x-10,y);
				textcolor(WHITE);
				textbackground(BLACK);
				borderline(80,24,x-10,y);
				printf("APPLICATION \"Supreme_Sudoku\" TERMINATED.\n\n");
				gotoxy(x-2,wherey());
				delprnt("Closing terminal",100,wherex(),wherey());
				delprnt(".........",50,wherex(),wherey());
				ext=1;}
				else {ext=0;}
				break;}
			case '`':break;
			case 'S':
			case 's':
			case 'M':
			case 'm':
			case 'O':
			case 'o':{settings(x,y);break;}
			case 'C':
			case 'c':{credits(x,y);break;}
			default:{;}
		}
	}
	}
	return 0;
}