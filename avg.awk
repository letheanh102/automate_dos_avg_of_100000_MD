{
    key[FNR] = $1
    for (colNr=1; colNr<=NF; colNr++) {
        sum[FNR,colNr] += $colNr 
    }
}
END {
    for (rowNr=1; rowNr<=FNR; rowNr++) {
        #printf "%s%s", key[rowNr], OFS
        for (colNr=1; colNr<=NF; colNr++) {
            printf "%s%s", (sum[rowNr,colNr]/ARGIND), (colNr<NF ? OFS : ORS)
        }
    }
}

