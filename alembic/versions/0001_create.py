""" Initial rev of database -- this should always be the first alembic version

Revision ID: 0000001
Revises: None
Create Date: 2014-10-28 14:14:45.896256

"""

# revision identifiers, used by Alembic.
revision = '00000001'
down_revision = None

from alembic import op


def upgrade():


    op.execute('''INSERT INTO rel_user (user_id, rel_lookup, attribute)
        VALUES
            (2, 'LOCATION', 'USA')
    ''')

    op.execute('''UPDATE user
                SET point_balance = 1000
                WHERE user_id=1;
    ''')

    op.execute('''UPDATE user
                SET tier = 'Silver'
                WHERE user_id=3;
    ''')

def downgrade():
    op.execute("TRUNCATE TABLE user")
    op.execute("TRUNCATE TABLE rel_user")
    op.execute("TRUNCATE TABLE rel_user_multi")
