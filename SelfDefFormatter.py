
def y_update_scale_value(temp,position):
    result=temp/1000
    return "{}K".format(int(result))
                        
def x_update_scale_value(temp,position):
    return "{}d".format(int(temp))