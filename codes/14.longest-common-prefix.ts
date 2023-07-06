/*
 * @lc app=leetcode id=14 lang=typescript
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
function longestCommonPrefix(strs: string[]): string {
    let minlen:number = Number.MAX_VALUE;
    let n:number = strs.length;
    for(let i=0;i<n;i++){
        minlen = Math.min(minlen,strs[i].length);
    }

    for(let i=0;i<minlen;i++){
        let letter:string = strs[0][i];
        for(let j=1;j<n;j++){
            if (letter != strs[j][i]){
                return strs[0].substring(0,i);
            }
        }
    }
    return strs[0].substring(0,minlen);
};
// @lc code=end

