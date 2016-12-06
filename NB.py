DATA = [
        ["1", "S", "-1"],
        ["1", "M", "-1"],
        ["1", "M", "1"],
        ["1", "S", "1"],
        ["1", "S", "-1"],
        ["2", "S", "-1"],
        ["2", "M", "-1"],
        ["2", "M", "1"],
        ["2", "L", "1"],
        ["2", "L", "1"],
        ["3", "L", "1"],
        ["3", "M", "1"],
        ["3", "M", "1"],
        ["3", "L", "1"],
        ["3", "L", "-1"],
]

def bayes_predict(p_label, p_attr, n_attr_sample, sample = ["3", "S"]):
    p_max = 0
    ret_label = None
    for label in p_label.keys():
        p = p_label[label]
        for i in range(n_attr_sample-1):
            p *= p_attr[i][label][sample[i]]
        if p >= p_max:
            p_max = p 
            ret_label = label
    return ret_label

def bayes_train(data = DATA):
    #sample attribute number
    n_attr_sample = len(DATA[0])
    #sample number
    n_sample = len(DATA)
    #get attr value set
    attr_values = [{} for i in range(n_attr_sample)]
    for sample in DATA:
        for i in range(n_attr_sample):
            if sample[i] in attr_values[i]:
                attr_values[i][sample[i]] += 1
            else:
                attr_values[i][sample[i]] = 1
    #class probability
    p_label = {}
    for label in attr_values[-1].keys():
        p_label[label] = 1.0*attr_values[-1][label]/n_sample
    #attribute probability
    p_attr = []
    #for each attribute
    for i in range(n_attr_sample-1):
        p_attr_i = {}
        #for each lable
        for label in attr_values[-1].keys():
            p_attr_i[label]={}
            #for each attr value
            Sr = len(attr_values[i].keys())
            for attr_v in attr_values[i].keys():
                #compute probability
                n_p = 0
                for sample in DATA:
                    if(sample[-1] == label and sample[i]==attr_v):
                        n_p+=1
                p_attr_i[label][attr_v] = (1.0*n_p)/(attr_values[-1][label])
        p_attr.append(p_attr_i)
    return p_label, p_attr, n_attr_sample

def main():
    p_label, p_attr, n_attr_sample = bayes_train()
    print(p_label,"\n" ,p_attr,"\n", n_attr_sample,"\n")
    ret_label = bayes_predict(p_label, p_attr, n_attr_sample)
    print(ret_label)

if __name__ == "__main__":
    main()