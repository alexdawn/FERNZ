from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(id='electric_arc_furnace',
                             processed_cargos_and_output_ratios=[('SCMT', 6), ('QLME', 2)],
                             combined_cargos_boost_prod=True,
                             prod_cargo_types=[('STEL', 6), ('SLAG', 2)],
                             prob_in_game='3',
                             prob_random='5',
                             prod_multiplier='[0, 0]',
                             map_colour='209',
                             name='string(STR_IND_ELECTRIC_ARC_FURNACE)',
                             nearby_station_name='string(STR_STATION_FURNACE)',
                             fund_cost_multiplier='160',
                             intro_year=1832)

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(id='electric_arc_furnace_tile_1',
                  animation_length=71,
                  animation_looping=True,
                  animation_speed=2,
                  custom_animation_control={'macro': 'random_first_frame',
                                            'animation_triggers': 'bitmask(ANIM_TRIGGER_INDTILE_CONSTRUCTION_STATE)'},
                  location_checks=TileLocationChecks(require_effectively_flat=True,
                                                     disallow_industry_adjacent=True))

sprite_ground = industry.add_sprite(
    sprite_number='GROUNDTILE_MUD_TRACKS'  # ground tile same as overlay tile
)
sprite_ground_overlay = industry.add_spriteset(
    type='empty',
)
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 76, -31, -45)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 76, -31, -45)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 63, -31, -32)],
)
spriteset_scrap_1 = industry.add_spriteset(
    sprites=[(220, 10, 64, 63, -31, -32)],
)
spriteset_scrap_2 = industry.add_spriteset(
    sprites=[(290, 10, 64, 63, -31, -32)],
)
spriteset_metal_1 = industry.add_spriteset(
    sprites=[(360, 10, 64, 63, -31, -32)],
)
spriteset_metal_2 = industry.add_spriteset(
    sprites=[(430, 10, 64, 63, -31, -32)],
)
spriteset_crane_1 = industry.add_spriteset(
    sprites=[(500, 10, 64, 63, -31, -32)],
)
spriteset_crane_2 = industry.add_spriteset(
    sprites=[(570, 10, 64, 63, -31, -32)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-5,
    yoffset=0,
    zoffset=40,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type='white_smoke_small',
    xoffset=-5,
    yoffset=5,
    zoffset=40,
)

industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_empty',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_2],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_3',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_3],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_scrap_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_scrap_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_scrap_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_scrap_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_crane_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crane_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_crane_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_crane_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_metal_1',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_metal_1],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_spritelayout(
    id='electric_arc_furnace_spritelayout_metal_2',
    ground_sprite=sprite_ground,
    ground_overlay=sprite_ground_overlay,
    building_sprites=[spriteset_metal_2],
    fences=['nw', 'ne', 'se', 'sw']
)
industry.add_industry_layout(
    id='electric_arc_furnace_industry_layout_1',
    layout=[(0, 0, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_2'),
            (0, 1, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_2'),
            (0, 2, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_2'),
            (0, 3, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_3'),
            (0, 4, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_3'),
            (1, 0, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_1'),
            (1, 1, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_1'),
            (1, 2, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_1'),
            (1, 3, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_scrap_1'),
            (1, 4, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_scrap_1'),
            (2, 0, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_metal_2'),
            (2, 1, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_metal_1'),
            (2, 2, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_empty'),
            (2, 3, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_crane_1'),
            (2, 4, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_scrap_1'),
            (3, 0, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_metal_2'),
            (3, 1, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_crane_2'),
            (3, 2, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_empty'),
            (3, 3, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_scrap_2'),
            (3, 4, 'electric_arc_furnace_tile_1', 'electric_arc_furnace_spritelayout_crane_1'),
            ]
)
