# -*- coding: utf-8 -*-

import click
from urls import DROPLETS
from base_request import DigitalOcean, print_table, CONTEXT_SETTINGS


@click.group()
def droplet_actions_group():
	"""
	droplet actions command group
	"""
	pass


def validate(dic):
	return True


@droplet_actions_group.command(name='droplet-actions', context_settings=CONTEXT_SETTINGS)
@click.option('--disable-backups', '-d', type=int, help='Disable backups for given droplet id', metavar='<3812352>')
@click.option('--reboot', '-r', type=int, help='Reboot droplet for given droplet id', metavar='<3812352>')
@click.pass_context
def droplet_actions(ctx, disable_backups, reboot):
	"""
	Droplet actions are tasks that can be executed on a Droplet.
	These can be things like rebooting, resizing, snapshotting, etc.
	"""

	if (not ctx.params['disable_backups'] and not ctx.params['reboot']):
		return click.echo(ctx.get_help())

	if validate(ctx.params):
		if disable_backups:
			method = 'POST'
			url = DROPLETS + str(disable_backups) + '/actions'
			params = {'type':'disable_backups'}
			result = DigitalOcean.do_request(method, url, token=token, proxy=proxy, params=params)
			if result['has_error']:
				click.echo()
				click.echo('Error: %s' %(result['error_message']))
			else:
				record = 'droplet disable backups'
				headers = ['Fields', 'Values']
				table = [['Id', result['action']['id']], ['Status', result['action']['status']], ['Type', result['action']['type']], ['Started at', result['action']['started_at']], ['Completed at', result['action']['completed_at']], ['Resource Id', result['action']['resource_id']], ['Resource Type', result['action']['resource_type']], ['Region', result['action']['region']]]
				data = {'headers': headers, 'table_data': table}
				print_table(tablefmt, data, record)
				click.echo()
				click.echo('To get status update of above action execute following command.')
				click.echo('Command: docli action -i %d' % disable_backups)

		if reboot:
			method = 'POST'
			url = DROPLETS + str(reboot) + '/actions'
			params = {'type':'reboot'}
			result = DigitalOcean.do_request(method, url, token=token, proxy=proxy, params=params)
			if result['has_error']:
				click.echo()
				click.echo('Error: %s' %(result['error_message']))
			else:
				record = 'droplet reboot'
				headers = ['Fields', 'Values']
				table = [['Id', result['action']['id']], ['Status', result['action']['status']], ['Type', result['action']['type']], ['Started at', result['action']['started_at']], ['Completed at', result['action']['completed_at']], ['Resource Id', result['action']['resource_id']], ['Resource Type', result['action']['resource_type']], ['Region', result['action']['region']]]
				data = {'headers': headers, 'table_data': table}
				print_table(tablefmt, data, record)
				click.echo()
				click.echo('To get status update of above action execute following command.')
				click.echo('Command: docli action -i %d' % reboot)