from pymongo import MongoClient
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


def make_plot(filt={}):
    client = MongoClient()
    runs = client.sacred.runs.find(filt)[client.sacred.runs.find(filt).count()-1]
    means = [x['mean'] for x in runs['info']['runs_info']]
    means = [means[x:x + runs['config']['pop']] for x in range(0, len(means), runs['config']['pop'])]
    feature_list = [x['parameters']['feature'] for x in runs['info']['runs_info']]
    feature_list = [feature_list[x:x + runs['config']['pop']] for x in range(0,
                                                                             len(feature_list),
                                                                             runs['config']['pop'])]
    feature_dict = {}
    for feature in runs['config']['parameter_options']['feature']['value']:
        counter_prepare = [[1 if feature in x else 0 for x in li] for li in feature_list]
        feature_dict[feature] = [sum(x) for x in counter_prepare]

    result_dict = {'means': means,
                   'feature_count': feature_dict}
    return result_dict


def plot_feature(result_dict, feature,  name=''):
    plt.plot(result_dict['feature_count'][feature], label=feature)
    plt.legend(loc='lower right')
    plt.ylabel('Number of features')
    plt.xlabel('Epoch')
    plt.savefig("".join([name, feature, "rys.pdf"]), dpi=72)
    plt.clf()


def plot_means(result_dict, name='mean'):
    best = [max(x) for x in result_dict['means']]
    plt.plot(best, label='Best in epoch')
    plt.legend(loc='lower right')
    plt.ylabel('Mean accuracy')
    plt.xlabel('Epoch')
    plt.savefig("".join([name, "_rys.pdf"]), dpi=72)
    plt.clf()

def plot_all_features(result_dict, name='features'):
    for feature in result_dict['feature_count']:
        plt.plot(result_dict['feature_count'][feature], label=feature)
    plt.legend(loc='lower right')
    plt.ylabel('Number of features')
    plt.xlabel('Epoch')
    plt.savefig("".join([name, "rys.pdf"]), dpi=72)
    plt.clf()
    
if __name__=='__main__':
    feature_dict = make_plot()
    plot_all_features(feature_dict)