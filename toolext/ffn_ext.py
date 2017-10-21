import ffn
import fix_yahoo_finance as yfx

@ffn.utils.memoize
def yf_fix(ticker, field, start=None, end=None, mrefresh=False):
    if field is None:
        field = 'Adj Close'

    tmp = yfx.download(ticker, start=start, end=end)

    if tmp is None:
        raise ValueError('failed to retrieve data for %s:%s' % (ticker, field))

    if field:
        return tmp[field]
    else:
        return tmp

def yf_override():
    try:
        ffn.data.yf = yf_fix
        print('repalce ffn.data.yf with fix_yahoo_finance toolkit')
    except:
        pass