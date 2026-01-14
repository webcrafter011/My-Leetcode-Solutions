class Solution:
    def separateSquares(self, squares):
        # prepare unique x and y coordinates
        xs = []
        ys = []
        for x, y, l in squares:
            xs.append(x); xs.append(x + l)
            ys.append(y); ys.append(y + l)
        xs = sorted(set(xs))
        ys = sorted(set(ys))

        # map x -> index; segments are between xs[i] and xs[i+1]
        xi = {v: i for i, v in enumerate(xs)}
        M = len(xs) - 1
        if M <= 0:
            # degenerate, no horizontal measure
            return float(min(y for _, y, _ in squares))

        # events at each Y value: start (add) and end (remove) lists of (l_idx, r_idx)
        from collections import defaultdict
        starts = defaultdict(list)
        ends = defaultdict(list)
        for x, y, l in squares:
            x1, x2 = x, x + l
            lidx = xi[x1]
            ridx = xi[x2]
            starts[y].append((lidx, ridx))
            ends[y + l].append((lidx, ridx))

        # segment tree for union length along x
        size = 4 * (M + 5)
        cover = [0] * size
        seglen = [0.0] * size

        # local references for speed
        xs_local = xs

        def update(node, l, r, ql, qr, val):
            if ql >= r or qr <= l:
                return
            if ql <= l and r <= qr:
                cover[node] += val
            else:
                mid = (l + r) // 2
                update(node * 2, l, mid, ql, qr, val)
                update(node * 2 + 1, mid, r, ql, qr, val)
            if cover[node] > 0:
                seglen[node] = xs_local[r] - xs_local[l]
            else:
                if l + 1 == r:
                    seglen[node] = 0.0
                else:
                    seglen[node] = seglen[node * 2] + seglen[node * 2 + 1]

        # sweep Y slabs, maintain active x-intervals and compute slab union length
        total_area = 0.0
        slab_lengths = []  # list of (y_bottom, y_top, union_x_length)
        K = len(ys)
        # iterate Y points; at position ys[i] we first remove those ending at this Y,
        # then add those starting at this Y. After that active set corresponds to interior (ys[i], ys[i+1]).
        for i in range(K - 1):
            y = ys[i]
            # remove intervals that end exactly at y
            for lidx, ridx in ends.get(y, ()):
                update(1, 0, M, lidx, ridx, -1)
            # add intervals that start exactly at y
            for lidx, ridx in starts.get(y, ()):
                update(1, 0, M, lidx, ridx, 1)

            length = seglen[1]  # union x-length across this slab
            y_top = ys[i + 1]
            h = y_top - y
            slab_area = length * h
            if slab_area > 0:
                slab_lengths.append((y, y_top, length))
                total_area += slab_area
            else:
                # still record zero-length slab to keep indexing logic simple
                slab_lengths.append((y, y_top, 0.0))

        half = total_area / 2.0

        # find the slab where cumulative area crosses half
        cum = 0.0
        for y_bot, y_top, length in slab_lengths:
            slab_h = y_top - y_bot
            slab_area = length * slab_h
            if cum + slab_area + 1e-12 < half:
                cum += slab_area
                continue
            # answer lies in this slab
            if length == 0.0:
                # if length zero but area needed, move to next non-zero; defensively handle floating error
                continue
            needed = half - cum
            H = y_bot + needed / length
            return float(H)
        # If we never returned (possible numerical edge), return topmost y
        return float(ys[-1])
