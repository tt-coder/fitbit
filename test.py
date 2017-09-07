import matplotlib
from mpl_toolkits.axes_grid.parasite_axes import SubplotHost
matplotlib.use('Agg')
import pylab
 
dam_player_ret = [31074, 16661, 33495, 22153, 22812, 36667, 28225, 25140, 24533, 6367, 20797, 22421, 10797, 7678, 20082, 15227, 3121, 7915, 14410, 11005, 25274, 17207, 12343, 12841, 25924, 18106, 26027, 22260, 27397, 23639, 26389, 20337, 16724, 20660]
kill_ret = [1, 0, 1, 0, 0, 2, 2, 3, 2, 0, 3, 1, 0, 1, 0, 3, 0, 2, 3, 7, 0, 1, 6, 1, 4, 2, 2, 1, 0, 0, 1, 4, 2, 0] 
dead_ret = [0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 2, 0, 2, 0, 0, 1, 0, 0, 1, 2, 0, 0, 2, 0, 1, 2, 2, 0, 0, 2, 1] 
 
_len = len(dam_player_ret)
_range = range(0, _len)
 
fig = matplotlib.pyplot.figure(1)
host = SubplotHost(fig, 111)
par1 = host.twinx()
par2 = host.twinx()
par1.axis["right"].set_visible(True)
 
offset = 60, 0
new_axisline = par2.get_grid_helper().new_fixed_axis
par2.axis["right2"] = new_axisline(loc="right", axes=par2, offset=offset)
par2.axis["right2"].label.set_visible(True)
par2.axis["right2"].set_label("dead")
 
fig.add_axes(host)
matplotlib.pyplot.subplots_adjust(right=0.75)
 
host.set_xlim(0, _len)
host.set_ylim(0, 40000)
host.set_xlabel("times")
host.set_ylabel("damage")
par1.set_ylabel("kill")
 
p1, = host.plot(_range, dam_player_ret, label="damage")
p2, = par1.plot(_range, kill_ret, label="kill")
p3, = par1.plot(_range, dead_ret, label="dead")
 
par1.set_ylim(0, 20)
par2.set_ylim(0, 20)
 
host.legend()
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
 
matplotlib.pyplot.draw()
matplotlib.pyplot.savefig('test.png')
