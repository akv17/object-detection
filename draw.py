_PLT = None
FIG_SIZE = (30, 30)


def _load_plt():
    global _PLT
    if _PLT is None:
        import platform
        import matplotlib
        if platform.system() == 'Darwin':
            matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        _PLT = plt
    return _PLT


def draw_arr(arr, size=FIG_SIZE):
    plt = _load_plt()
    plt.figure(figsize=size)
    plt.imshow(arr, cmap='gray')


def draw_rects(rects, color='r', alpha=0.5, do_enumerate=False):
    plt = _load_plt()
    for i, (y_min, y_max, x_min, x_max) in enumerate(rects):
        plt.plot([x_min, x_min], [y_min, y_max], color=color, alpha=alpha)
        plt.plot([x_max, x_max], [y_min, y_max], color=color, alpha=alpha)
        plt.plot([x_min, x_max], [y_min, y_min], color=color, alpha=alpha)
        plt.plot([x_min, x_max], [y_max, y_max], color=color, alpha=alpha)
        if do_enumerate:
            plt.text(x_min, y_min, str(i))


def draw_points(points, color='r', alpha=0.5):
    plt = _load_plt()
    ys = [p[0] for p in points]
    xs = [p[1] for p in points]
    plt.scatter(xs, ys, color=color, alpha=alpha)


def draw(calls, fp=None):
    plt = _load_plt()
    for i, (func, kwargs) in enumerate(calls):
        func(**kwargs)
        if i == len(calls) - 1 and fp is None:
            plt.show()
    if fp is not None:
        plt.savefig(fp)
        plt.close()
