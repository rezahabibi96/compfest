from orator.migrations import Migration


class CreatUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        if not self.schema.has_table('users'):
            with self.schema.create('users') as table:
                table.increments('id')
                table.string('email', 225)
                table.string('password', 225)

    def down(self):
        """
        Revert the migrations.
        """
        pass
