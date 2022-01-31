
it = 1;
annotation = sprintf('%s', 'walk');

while(it <= 50) 

    %ARR_OUT = strings([4900,1]);
    
    strt = sprintf('%s%s%d%s', 'C:\Users\KimYongHwan\Documents\GitHub\2019-cap1-2019_22\src\190528_Dataset2\annotation_', annotation, it,'.dat.csv');
    fid = fopen(strt,'wt');
    k = 1;
    while(k < 4901)
        fprintf(fid,'%s\n',annotation);
        
        k = k + 1;
    end
    
    it = it + 1;
    fclose(fid);
end


