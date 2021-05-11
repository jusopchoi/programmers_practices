#include <stdio.h>
#include <string.h>
#define MAX_N 500
int N, dp[MAX_N];
int course[MAX_N][2];
int moving[MAX_N][MAX_N];
int max(int a, int b){
    if(a>b)
        return a;
    return b;
}
int find_dp(int origin){
    if(dp[origin] != -1)
        return(dp[origin]);
    int i, partial_time;
    dp[origin] = 0;
    for(i = 0; i < N; i++){
        if(i==origin)
            continue;
        partial_time = course[i][1] - max(course[origin][1] + moving[origin][i], course[i][0]);
        if(partial_time > 0){
            dp[origin] = max(dp[origin], partial_time + find_dp(i));
        }
    }
    return(dp[origin]);
}
int main(void)
{
	int test_case;
	int T;
	setbuf(stdout, NULL);
	scanf("%d", &T);
	for (test_case = 1; test_case <= T; ++test_case)
	{
		/////////////////////////////////////////////////////////////////////////////////////////////
		int s, i, j, k, partial_time, max_time = 0;
		scanf("%d %d", &N, &s);
        s--;
        for(i = 0; i < N; i++){
            scanf("%d %d", &course[i][0], &course[i][1]);
        }
        for(i = 0; i < N; i++){
            for(j = 0; j < N; j++){
                scanf("%d", &moving[i][j]);
            }
        }
        for(k = 0; k < N; k++){
            for(i = 0; i < N; i++){
                for(j = 0; j < N; j++){
                    if(moving[i][j] > moving[i][k] + moving[k][j])
                        moving[i][j] = moving[i][k] + moving[k][j];
                }
            }
        }
        memset(dp, -1, sizeof(dp));
        for(i = 0; i < N; i++){
            partial_time = course[i][1] - max(moving[s][i], course[i][0]);
            if(partial_time > 0){
                max_time = max(max_time, partial_time + find_dp(i));
            }
        }
		printf("#%d %d\n", test_case, max_time);
		/////////////////////////////////////////////////////////////////////////////////////////////
	}
	return 0; //정상종료시 반드시 0을 리턴해야 합니다.
}
