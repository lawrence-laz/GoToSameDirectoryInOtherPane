from fman import DirectoryPaneCommand

class GoToSameDirectoryInOtherPane(DirectoryPaneCommand):
	aliases = (
		'Go to same directory in other pane',
		'Go to same folder in other pane',
		'Open same directory in other pane', 
		'Open same folder in other pane'
		)

	def __call__(self):
		current_path = self.pane.get_path()
		other_pane = self._get_opposite_pane(self.pane)
		other_pane.set_path(current_path)

	def _get_opposite_pane(self, pane):
		panes = pane.window.get_panes()
		return panes[(panes.index(pane) + 1) % len(panes)]
