from orator.migrations import Migration


class CreatBalancesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        if not self.schema.has_table('balances'):
            with self.schema.create('balances') as table:
                table.increments('id')
                table.big_integer('amount')
                table.timestamp('date')

    def down(self):
        """
        Revert the migrations.
        """
        pass
