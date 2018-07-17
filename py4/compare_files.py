def compare_files(f1, f2, read_bytes=False):
    '''
    Python's file_cmp module has issues, particularly
    saying two files, one created on a mac and one on
    Windows, are different even though the content is 
    the same because of the line terminator issue.  Also,
    this prints out some useful info.
    
    This most recent version skips all whitespace only 
    lines.  This is because sometimes macs seem to skip
    whitespace only lines when reading.  This also means
    that line numbers reported by this routine might not
    match up with the display in a text editor on macs.
    '''
    if not read_bytes:
        f1 = open(f1)
        f2 = open(f2)
    else:
        f1 = open(f1, 'rb')
        f2 = open(f2, 'rb')
        
    f1_line_no = 0
    l1 = f1.readline()
    while l1.isspace():
        f1_line_no += 1
        l1 = f1.readline()
        
    f2_line_no = 0    
        
    while l1:
        f1_line_no += 1
        
        l2 = f2.readline()
        while l2.isspace():
            f2_line_no += 1
            l2 = f2.readline()

        if not l2:
            print('\n************ MISSING LINE ***************')
            print('file 1 line number:', f1_line_no)
            print('missing line in file 2, no match for file 1 line:')
            print(repr(l1))
            print('*****************************************\n')
            return False
        else: f2_line_no += 1
        
        l1 = l1.rstrip() # avoid cross-platform eol character issues
        l2 = l2.rstrip()
        if l1 != l2:
            print('\n************ FILE MISMATCH ***************')
            print('mismatch on line numbers (f1 - f2):', f1_line_no, '-', f2_line_no, '\n')
            print('file 1 line:', repr(l1), '\n')
            print('file 2 line:', repr(l2), '\n')
            print('******************************************\n')
            i = 0
            while i < len(l1):
                if i == len(l2):
                    print('l2 shorter, missing character', repr(l1[i]), 'at position', i, '\n')
                    return False
                if l1[i] != l2[i]:
                    print('character mismatch at position', str(i) + ':', repr(l1[i]), '!=', repr(l2[i]), '\n')
                    return False
                i += 1
            print('l1 shorter, missing character', repr(l2[i]), 'at position', i - 1, '\n')
            return False
        l1 = f1.readline()
        while l1.isspace():
            f1_line_no += 1
            l1 = f1.readline()
            
    l2 = f2.readline()
    while l2.isspace():
        f2_line_no += 1
        l2 = f2.readline()
    if l2:
        print('\n************ MISSING LINE ***************')
        print('file 2 line number:', f2_line_no + 1)
        print('extra line in file2, no match in file 1 for:')
        print(repr(l2))
        print('*****************************************\n')
        return False
        
    return True
